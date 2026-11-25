"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                # đồng cho 1.000 token đầu vào
GIA_RA = 130                # đồng cho 1.000 token đầu ra
GIA_TOOL = 15               # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000           # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000            # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    khong_thanh_cong = len(reqs) - thanh_cong
    he_thong = tong + khong_thanh_cong * BASELINE

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        khong_thanh_cong=khong_thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
        he_thong=he_thong,
        he_thong_moi_yc=he_thong / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Hàm tính cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def in_nhiem_vu_a(runs, reqs):
    print('\n=== NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    print(f"Token (đo từ trace):                  {kq['token']:>12,.0f} đ")
    print(f"Tool (đo từ trace, {int(runs['tool_calls'].sum()):,} lần):     {kq['tool']:>12,.0f} đ")
    print(f"  Trong đó lần chạy 2 & 3:            {kq['chay_lai']:>12,.0f} đ")
    print(f"Xem lại [simulated] ({reqs['phut_xem_lai_simulated'].sum():.0f} phút):   {kq['xem_lai']:>12,.0f} đ")
    print(f"Làm lại [simulated] ({reqs['phut_lam_lai_simulated'].sum():.0f} phút):  {kq['lam_lai']:>12,.0f} đ")
    print(f"Tổng chi phí [có phần simulated]:     {kq['tong']:>12,.0f} đ")
    print(f"Số việc thành công:                   {kq['thanh_cong']:>12,d} / {len(reqs):,d}")
    print(f"Chi phí mỗi việc thành công [sim]:    {kq['cps']:>12,.0f} đ")
    print(f"Hoá đơn token+tool / yêu cầu:         {kq['hoa_don_moi_yc']:>12,.1f} đ")
    print(f"Gấp hoá đơn / yêu cầu:                {kq['cps'] / kq['hoa_don_moi_yc']:>12,.1f} lần")
    print(f"Tỉ trọng làm lại / xem lại [sim]:     {kq['lam_lai']/kq['tong']*100:.1f}% / {kq['xem_lai']/kq['tong']*100:.1f}%")
    print(f"Chi phí cả hệ thống / yêu cầu [sim]:  {kq['he_thong_moi_yc']:>12,.0f} đ ({kq['he_thong_moi_yc']/BASELINE:.2f}× của 12.000 đ)")

    print('\n=== NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':12s} {'Số YC':>6s} {'Thành công':>11s} {'Lần/YC':>8s} {'CPS [sim]':>12s} {'So 12k':>8s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        tl = r['thanh_cong'] / len(sub) * 100
        lan = sub['so_lan_chay'].mean()
        print(f"{loai:12s} {len(sub):>6d} {tl:>10.1f}% {lan:>8.2f} {r['cps']:>10,.0f} đ {r['cps']/BASELINE:>7.2f}×")

    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    piv = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print('\nTỉ lệ status == ok theo từng lần thử (%):')
    print(piv.round(1).to_string())

    print('\n=== NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, pv)
    for ten, kl_thang in [('45.000 yêu cầu/tháng', 45_000), ('Một nửa khối lượng (22.500)', 22_500)]:
        viec_thang = kl_thang * r_pv['thanh_cong'] / len(reqs)
        co_dinh_viec = CHI_PHI_CO_DINH / viec_thang
        tong_cps = r_pv['cps'] + co_dinh_viec
        print(f"{ten:28s}: {viec_thang:>8,.0f} việc/tháng | cố định {co_dinh_viec:>6,.0f} đ | tổng {tong_cps:>6,.0f} đ ({tong_cps/BASELINE:.2f}×) [sim]")
    return kq


def in_nhiem_vu_b(runs, reqs, kq_goc):
    print('\n=== NHIỆM VỤ B1 & B2 · BẢNG ĐỘ NHẠY ===')
    goc = kq_goc['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    print(f"{'Kịch bản':30s} {'CPS [sim]':>12s} {'Thay đổi':>10s}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:30s} {cps:>10,.0f} đ {(cps / goc - 1) * 100:>+9.1f}%")

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"{'B2 · Token×2 + Xem lại×2':30s} {cap:>10,.0f} đ {(cap / goc - 1) * 100:>+9.1f}%")

    print('\n=== NHIỆM VỤ B3 · GIỚI HẠN CHẠY LẠI & CHI PHÍ CẢ HỆ THỐNG ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý [sim]':>18s} {'Không TC':>10s} {'Cả hệ thống [sim]':>18s} {'CPS [sim]':>12s}")
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        print(f"{k} lần     {r['tong']:>16,.0f} đ {r['khong_thanh_cong']:>10d} {r['he_thong']:>16,.0f} đ {r['cps']:>10,.0f} đ")

    print('\n=== NHIỆM VỤ B4 · XEM LẠI 100% (noi_dia + hang_nang) ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    yc_co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    token_tool = (runs_pv['tokens_in'] / 1000 * GIA_VAO
                  + runs_pv['tokens_out'] / 1000 * GIA_RA
                  + runs_pv['tool_calls'] * GIA_TOOL).sum()
    phut_ll_thuc = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()

    for nhan, phut_ll in [('Giả định đề (9 phút/ca)', 9.0), (f'Trung bình dữ liệu ({phut_ll_thuc:.1f} phút/ca)', phut_ll_thuc)]:
        tien_xl = yc_co_ok * 5 * LUONG_PHUT
        tien_ll = ca_lam_lai * phut_ll * LUONG_PHUT
        tong = token_tool + tien_xl + tien_ll
        cps = tong / thanh_cong
        hoa_von_phut = (BASELINE * thanh_cong - token_tool - tien_ll) / (yc_co_ok * LUONG_PHUT)
        print(f"{nhan}: tổng {tong:,.0f} đ -> CPS = {cps:,.0f} đ ({cps/BASELINE:.2f}×) [sim] | hoà vốn xem lại <= {hoa_von_phut:.1f} phút")


def in_nhiem_vu_d1(reqs):
    print('\n=== NHIỆM VỤ D1 · CỠ MẪU & TỈ LỆ AN TOÀN HIỆN TẠI ===')
    icc = 0.02
    n_5 = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_5 * de_75)
    so_nv_nhom = math.ceil(n_nv_75 / 75)
    n_eff_20 = 20 / icc
    n_eff_6 = 6 / icc
    n_6 = co_mau(0.70, 0.76)
    m_min = math.ceil(n_6 * (1 - icc) / (20 - n_6 * icc))
    de_6 = 1 + (m_min - 1) * icc

    h_5 = proportion_effectsize(0.75, 0.70)
    power_5_tai_n859 = NormalIndPower().power(effect_size=abs(h_5), nobs1=n_6, alpha=0.05, ratio=1.0)

    print(f"a) Chia theo yêu cầu (MDE +5 điểm):       {n_5:,d} yêu cầu/nhóm")
    print(f"b) Theo nhân viên (m=75, DE={de_75:.2f}):       {n_nv_75:,d} yc/nhóm -> {so_nv_nhom} người/nhóm (tổng {so_nv_nhom*2} > 40: không đủ)")
    print(f"c) 20 nhân viên/nhóm (c/ICC):             tối đa {n_eff_20:,.0f} < {n_5:,d} (không đạt MDE 5 điểm)")
    print(f"d) 6 depot/nhóm (c/ICC):                  tối đa {n_eff_6:,.0f} (không đạt, dưới 20 cụm)")
    print(f"e) MDE +6 điểm (n={n_6}/nhóm), 20 nv/nhóm:  m >= {m_min} yc/người (DE = {de_6:.2f})")
    print(f"   Power nếu tác động thật 5 điểm (n={n_6}): {power_5_tai_n859:.2f}")

    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(f"Tỉ lệ mo_lai_trong_7_ngay toàn bộ:        {reqs['mo_lai_trong_7_ngay'].mean()*100:.2f}% ({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)})")
    print(f"Tỉ lệ mo_lai_trong_7_ngay noi_dia+hn:     {pv['mo_lai_trong_7_ngay'].mean()*100:.2f}% ({int(pv['mo_lai_trong_7_ngay'].sum())}/{len(pv)})")


def in_nhiem_vu_e1(reqs):
    print('\n=== NHIỆM VỤ E1 · TÍNH THỬ BA CHỈ SỐ TRÊN 1.200 YÊU CẦU ===')
    chinh_cnt = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_cnt = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    an_toan_cnt = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    print(f"Chỉ số chính (đóng 24h & không mở lại 7d): {chinh_cnt/len(reqs)*100:.2f}% ({chinh_cnt}/{len(reqs)})")
    print(f"Chỉ số dùng (tỉ lệ bỏ qua sua+bo):         {bo_qua_cnt/len(xem)*100:.2f}% ({bo_qua_cnt}/{len(xem)})")
    print(f"Chỉ số an toàn (mở lại trong 7 ngày):      {an_toan_cnt/len(reqs)*100:.2f}% ({an_toan_cnt}/{len(reqs)})")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    kq_goc = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, kq_goc)
    in_nhiem_vu_d1(reqs)
    in_nhiem_vu_e1(reqs)
