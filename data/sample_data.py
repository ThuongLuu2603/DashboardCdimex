import pandas as pd
import numpy as np

def get_overview_data():
    return {
        'TH 2024': 132166,
        'KH 2025': 158500,
        'TH 2025': 140541,
        'KH 2026': 157400
    }

def get_khoi_data():
    return pd.DataFrame({
        'Khối': ['KD Truyền thống', 'TMĐT', 'Mảng khác'],
        'TH 2024': [127983, 3381, 803],
        'KH 2025': [154400, 3500, 600],
        'TH 2025': [136640, 3544, 357],
        'KH 2026': [150200, 7000, 200]
    })

def get_ban_data():
    return pd.DataFrame({
        'Ban': ['PT & TTNN', 'Đại học', 'Học liệu', 'KD TM & DV'],
        'TH 2025': [45000, 64340, 12800, 14500],
        'KH 2025': [45000, 72900, 22000, 14500],
        '% Đạt KH': [100, 88, 58, 100],
        'Lãi gộp 2025': [5175, 15658, 1792, 1812],
        'KH 2026': [50000, 69000, 16000, 15200]
    })

def get_thang_2026_data():
    return pd.DataFrame({
        'Tháng': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'],
        'Doanh thu': [6107, 7730, 9744, 13390, 11409, 11188, 14954, 15904, 13944, 17433, 13378, 22219],
        'Lãi gộp': [1041, 1259, 1647, 2537, 2133, 1835, 2432, 2554, 2453, 3222, 2570, 4311]
    })

def get_sanpham_data():
    return pd.DataFrame({
        'Nhóm sản phẩm': ['Sách ngoại văn', 'Học liệu', 'Đồ chơi giáo dục', 'Sản phẩm số', 'Dịch vụ'],
        'Doanh thu': [65000, 42000, 18000, 8500, 7041],
        'Tỷ trọng': [46.3, 29.9, 12.8, 6.0, 5.0]
    })

def get_khachhang_data():
    return pd.DataFrame({
        'Phân khúc': ['Trường Đại học', 'Trường PT Quốc tế', 'TTNN', 'B2C Online', 'B2C Offline', 'Khác'],
        'Doanh thu': [64340, 45000, 12800, 10500, 6000, 1901],
        'Tỷ trọng': [45.8, 32.0, 9.1, 7.5, 4.3, 1.4]
    })
