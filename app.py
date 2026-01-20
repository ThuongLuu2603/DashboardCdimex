from data.sample_data import (
    get_overview_data,
    get_khoi_data,
    get_ban_data,
    get_thang_2026_data,
    get_sanpham_data,
    get_khachhang_data
)

# Trong code, thay:
# data_khoi = pd.DataFrame({...})
# Thành:
data_khoi = get_khoi_data()
