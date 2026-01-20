

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from data.sample_data import (
    get_overview_data,
    get_khoi_data,
    get_ban_data,
    get_thang_2026_data,
    get_sanpham_data,
    get_khachhang_data
)

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="CDIMEX Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CSS TÙY CHỈNH ====================
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    h1 {
        color: #1f77b4;
        font-weight: bold;
    }
    h2 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== DỮ LIỆU MẪU ====================

# Dữ liệu tổng quan
data_overview = {
    'TH 2024': 132166,
    'KH 2025': 158500,
    'TH 2025': 140541,
    'KH 2026': 157400
}

# Dữ liệu theo khối
data_khoi = get_khoi_data()

# Dữ liệu theo Ban
data_ban = pd.DataFrame({
    'Ban': ['PT & TTNN', 'Đại học', 'Học liệu', 'KD TM & DV'],
    'TH 2025': [45000, 64340, 12800, 14500],
    'KH 2025': [45000, 72900, 22000, 14500],
    '% Đạt KH': [100, 88, 58, 100],
    'Lãi gộp 2025': [5175, 15658, 1792, 1812],
    'KH 2026': [50000, 69000, 16000, 15200]
})

# Dữ liệu theo tháng 2026
data_thang_2026 = pd.DataFrame({
    'Tháng': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12'],
    'Doanh thu': [6107, 7730, 9744, 13390, 11409, 11188, 14954, 15904, 13944, 17433, 13378, 22219],
    'Lãi gộp': [1041, 1259, 1647, 2537, 2133, 1835, 2432, 2554, 2453, 3222, 2570, 4311]
})

# Dữ liệu sản phẩm
data_sanpham = pd.DataFrame({
    'Nhóm sản phẩm': ['Sách ngoại văn', 'Học liệu', 'Đồ chơi giáo dục', 'Sản phẩm số', 'Dịch vụ'],
    'Doanh thu': [65000, 42000, 18000, 8500, 7041],
    'Tỷ trọng': [46.3, 29.9, 12.8, 6.0, 5.0]
})

# Dữ liệu khách hàng
data_khachhang = pd.DataFrame({
    'Phân khúc': ['Trường Đại học', 'Trường PT Quốc tế', 'TTNN', 'B2C Online', 'B2C Offline', 'Khác'],
    'Doanh thu': [64340, 45000, 12800, 10500, 6000, 1901],
    'Tỷ trọng': [45.8, 32.0, 9.1, 7.5, 4.3, 1.4]
})

# ==================== SIDEBAR ====================
with st.sidebar:
    st.image("https://via.placeholder.com/200x80/1f77b4/ffffff?text=CDIMEX", use_container_width=True)
    st.title("📊 CDIMEX Dashboard")
    st.markdown("---")
    
    dashboard_option = st.selectbox(
        "Chọn Dashboard",
        ["🏠 Tổng quan", "📈 Phân tích theo Khối/Ban", "📅 Xu hướng thời gian", 
         "🎯 Kế hoạch 2026", "📦 Phân tích sản phẩm", "👥 Phân tích khách hàng",
         "💰 Tài chính", "🎬 Executive Summary"]
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Bộ lọc")
    
    date_range = st.date_input(
        "Chọn khoảng thời gian",
        value=(datetime.now() - timedelta(days=365), datetime.now())
    )
    
    khoi_filter = st.multiselect(
        "Chọn Khối",
        options=data_khoi['Khối'].tolist(),
        default=data_khoi['Khối'].tolist()
    )
    
    st.markdown("---")
    st.info("💡 **Tip**: Hover vào biểu đồ để xem chi tiết")
    
    st.markdown("---")
    st.caption(f"Cập nhật: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# ==================== DASHBOARD 1: TỔNG QUAN ====================
if dashboard_option == "🏠 Tổng quan":
    st.title("🏠 Dashboard Tổng Quan Kinh Doanh")
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        delta_dt = ((140541 - 158500) / 158500) * 100
        st.metric(
            label="💰 Doanh thu 2025",
            value="140.5 tỷ",
            delta=f"{delta_dt:.1f}% vs KH",
            delta_color="inverse"
        )
    
    with col2:
        delta_lg = ((25610 - 29093) / 29093) * 100
        st.metric(
            label="💵 Lãi gộp 2025",
            value="25.6 tỷ",
            delta=f"{delta_lg:.1f}% vs KH",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            label="📊 Lãi trước thuế",
            value="3.1 tỷ",
            delta="65% vs KH",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="🎯 Tỷ lệ đạt KH",
            value="89%",
            delta="-11%",
            delta_color="inverse"
        )
    
    st.markdown("---")
    
    # Biểu đồ so sánh
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 So sánh Doanh thu qua các năm")
        
        fig_dt = go.Figure()
        
        years = ['TH 2024', 'KH 2025', 'TH 2025', 'KH 2026']
        values = [132166, 158500, 140541, 157400]
        colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71']
        
        fig_dt.add_trace(go.Bar(
            x=years,
            y=values,
            text=[f"{v:,.0f}" for v in values],
            textposition='outside',
            marker_color=colors,
            hovertemplate='<b>%{x}</b><br>Doanh thu: %{y:,.0f} triệu<extra></extra>'
        ))
        
        fig_dt.update_layout(
            height=400,
            yaxis_title="Triệu đồng",
            showlegend=False,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_dt, use_container_width=True)
    
    with col2:
        st.subheader("📈 Tỷ lệ tăng trưởng")
        
        growth_data = pd.DataFrame({
            'Kỳ': ['2024→2025 (KH)', '2024→2025 (TH)', '2025→2026 (KH)'],
            'Tăng trưởng (%)': [19.9, 6.3, 12.0]
        })
        
        fig_growth = go.Figure()
        
        fig_growth.add_trace(go.Bar(
            x=growth_data['Kỳ'],
            y=growth_data['Tăng trưởng (%)'],
            text=[f"{v:.1f}%" for v in growth_data['Tăng trưởng (%)']],
            textposition='outside',
            marker_color=['#2ecc71', '#e74c3c', '#3498db'],
            hovertemplate='<b>%{x}</b><br>Tăng trưởng: %{y:.1f}%<extra></extra>'
        ))
        
        fig_growth.update_layout(
            height=400,
            yaxis_title="Phần trăm (%)",
            showlegend=False
        )
        
        st.plotly_chart(fig_growth, use_container_width=True)
    
    st.markdown("---")
    
    # Gauge chart cho tỷ lệ đạt KH
    st.subheader("🎯 Tỷ lệ hoàn thành Kế hoạch 2025")
    
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=89,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "% Đạt KH", 'font': {'size': 24}},
        delta={'reference': 100, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#f39c12"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 60], 'color': '#e74c3c'},
                {'range': [60, 80], 'color': '#f39c12'},
                {'range': [80, 95], 'color': '#3498db'},
                {'range': [95, 100], 'color': '#2ecc71'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 100
            }
        }
    ))
    
    fig_gauge.update_layout(height=300)
    st.plotly_chart(fig_gauge, use_container_width=True)

# ==================== DASHBOARD 2: PHÂN TÍCH THEO KHỐI/BAN ====================
elif dashboard_option == "📈 Phân tích theo Khối/Ban":
    st.title("📈 Phân tích theo Khối/Ban")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Theo Khối", "🏢 Theo Ban", "🎯 Tỷ lệ đạt KH"])
    
    with tab1:
        st.subheader("Doanh thu theo Khối")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Stacked bar chart
            fig_khoi = go.Figure()
            
            periods = ['TH 2024', 'KH 2025', 'TH 2025', 'KH 2026']
            
            for khoi in data_khoi['Khối']:
                khoi_data = data_khoi[data_khoi['Khối'] == khoi]
                fig_khoi.add_trace(go.Bar(
                    name=khoi,
                    x=periods,
                    y=[khoi_data['TH 2024'].values[0], khoi_data['KH 2025'].values[0], 
                       khoi_data['TH 2025'].values[0], khoi_data['KH 2026'].values[0]],
                    hovertemplate='<b>%{fullData.name}</b><br>%{y:,.0f} triệu<extra></extra>'
                ))
            
            fig_khoi.update_layout(
                barmode='stack',
                height=400,
                yaxis_title="Triệu đồng",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            
            st.plotly_chart(fig_khoi, use_container_width=True)
        
        with col2:
            # Pie chart tỷ trọng 2025
            fig_pie = px.pie(
                data_khoi,
                values='TH 2025',
                names='Khối',
                title='Tỷ trọng TH 2025',
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            fig_pie.update_layout(height=400)
            
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab2:
        st.subheader("Doanh thu & Lãi gộp theo Ban")
        
        # Combo chart
        fig_ban = go.Figure()
        
        fig_ban.add_trace(go.Bar(
            name='Doanh thu TH 2025',
            x=data_ban['Ban'],
            y=data_ban['TH 2025'],
            marker_color='#3498db',
            yaxis='y',
            hovertemplate='<b>%{x}</b><br>Doanh thu: %{y:,.0f} triệu<extra></extra>'
        ))
        
        fig_ban.add_trace(go.Bar(
            name='Lãi gộp 2025',
            x=data_ban['Ban'],
            y=data_ban['Lãi gộp 2025'],
            marker_color='#2ecc71',
            yaxis='y',
            hovertemplate='<b>%{x}</b><br>Lãi gộp: %{y:,.0f} triệu<extra></extra>'
        ))
        
        # Tính tỷ suất lãi gộp
        ty_suat = (data_ban['Lãi gộp 2025'] / data_ban['TH 2025'] * 100).round(1)
        
        fig_ban.add_trace(go.Scatter(
            name='Tỷ suất lãi gộp (%)',
            x=data_ban['Ban'],
            y=ty_suat,
            yaxis='y2',
            mode='lines+markers+text',
            marker=dict(size=10, color='#e74c3c'),
            line=dict(width=3),
            text=[f"{v}%" for v in ty_suat],
            textposition='top center',
            hovertemplate='<b>%{x}</b><br>Tỷ suất: %{y:.1f}%<extra></extra>'
        ))
        
        fig_ban.update_layout(
            height=500,
            yaxis=dict(title='Triệu đồng'),
            yaxis2=dict(title='Tỷ suất lãi gộp (%)', overlaying='y', side='right'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_ban, use_container_width=True)
        
        # Bảng chi tiết
        st.subheader("📋 Chi tiết theo Ban")
        
        display_df = data_ban.copy()
        display_df['TH 2025'] = display_df['TH 2025'].apply(lambda x: f"{x:,.0f}")
        display_df['KH 2025'] = display_df['KH 2025'].apply(lambda x: f"{x:,.0f}")
        display_df['Lãi gộp 2025'] = display_df['Lãi gộp 2025'].apply(lambda x: f"{x:,.0f}")
        display_df['KH 2026'] = display_df['KH 2026'].apply(lambda x: f"{x:,.0f}")
        display_df['% Đạt KH'] = display_df['% Đạt KH'].apply(lambda x: f"{x}%")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    with tab3:
        st.subheader("🎯 Tỷ lệ hoàn thành Kế hoạch theo Ban")
        
        # Horizontal bar chart
        fig_hoan_thanh = go.Figure()
        
        colors = ['#2ecc71' if x >= 95 else '#3498db' if x >= 80 else '#f39c12' if x >= 60 else '#e74c3c' 
                  for x in data_ban['% Đạt KH']]
        
        fig_hoan_thanh.add_trace(go.Bar(
            y=data_ban['Ban'],
            x=data_ban['% Đạt KH'],
            orientation='h',
            marker_color=colors,
            text=[f"{v}%" for v in data_ban['% Đạt KH']],
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Đạt: %{x}% KH<extra></extra>'
        ))
        
        # Thêm line benchmark tại 100%
        fig_hoan_thanh.add_vline(x=100, line_dash="dash", line_color="red", 
                                  annotation_text="Mục tiêu 100%", annotation_position="top")
        
        fig_hoan_thanh.update_layout(
            height=400,
            xaxis_title="Phần trăm (%)",
            showlegend=False,
            xaxis=dict(range=[0, 110])
        )
        
        st.plotly_chart(fig_hoan_thanh, use_container_width=True)
        
        # Phân tích
        st.markdown("### 📊 Phân tích")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.success(f"✅ **Đạt KH**: {len(data_ban[data_ban['% Đạt KH'] >= 95])} Ban")
        
        with col2:
            st.warning(f"⚠️ **Gần đạt**: {len(data_ban[(data_ban['% Đạt KH'] >= 80) & (data_ban['% Đạt KH'] < 95)])} Ban")
        
        with col3:
            st.error(f"❌ **Chưa đạt**: {len(data_ban[data_ban['% Đạt KH'] < 80])} Ban")

# ==================== DASHBOARD 3: XU HƯỚNG THỜI GIAN ====================
elif dashboard_option == "📅 Xu hướng thời gian":
    st.title("📅 Xu hướng theo Thời gian")
    
    st.subheader("📈 Doanh thu & Lãi gộp theo tháng (Kế hoạch 2026)")
    
    # Line chart với 2 trục Y
    fig_thang = go.Figure()
    
    fig_thang.add_trace(go.Scatter(
        x=data_thang_2026['Tháng'],
        y=data_thang_2026['Doanh thu'],
        name='Doanh thu',
        mode='lines+markers',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8),
        yaxis='y',
        hovertemplate='<b>%{x}</b><br>Doanh thu: %{y:,.0f} triệu<extra></extra>'
    ))
    
    fig_thang.add_trace(go.Scatter(
        x=data_thang_2026['Tháng'],
        y=data_thang_2026['Lãi gộp'],
        name='Lãi gộp',
        mode='lines+markers',
        line=dict(color='#2ecc71', width=3),
        marker=dict(size=8),
        yaxis='y2',
        hovertemplate='<b>%{x}</b><br>Lãi gộp: %{y:,.0f} triệu<extra></extra>'
    ))
    
    # Highlight mùa cao điểm
    cao_diem = [3, 6, 7, 9, 11]  # Tháng 4, 7, 8, 10, 12
    for idx in cao_diem:
        fig_thang.add_vrect(
            x0=idx-0.5, x1=idx+0.5,
            fillcolor="yellow", opacity=0.1,
            layer="below", line_width=0,
        )
    
    fig_thang.update_layout(
        height=500,
        yaxis=dict(title='Doanh thu (triệu đồng)', side='left'),
        yaxis2=dict(title='Lãi gộp (triệu đồng)', overlaying='y', side='right'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_thang, use_container_width=True)
    
    st.info("💡 **Vùng tô vàng**: Tháng cao điểm (T4, T7, T8, T10, T12)")
    
    st.markdown("---")
    
    # Area chart
    st.subheader("📊 Xu hướng tích lũy")
    
    data_thang_2026['Doanh thu tích lũy'] = data_thang_2026['Doanh thu'].cumsum()
    data_thang_2026['Lãi gộp tích lũy'] = data_thang_2026['Lãi gộp'].cumsum()
    
    fig_area = go.Figure()
    
    fig_area.add_trace(go.Scatter(
        x=data_thang_2026['Tháng'],
        y=data_thang_2026['Doanh thu tích lũy'],
        name='Doanh thu tích lũy',
        fill='tozeroy',
        line=dict(color='#3498db'),
        hovertemplate='<b>%{x}</b><br>Tích lũy: %{y:,.0f} triệu<extra></extra>'
    ))
    
    fig_area.update_layout(
        height=400,
        yaxis_title="Triệu đồng",
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_area, use_container_width=True)
    
    # Bảng dữ liệu
    st.subheader("📋 Dữ liệu chi tiết")
    
    display_thang = data_thang_2026[['Tháng', 'Doanh thu', 'Lãi gộp']].copy()
    display_thang['Doanh thu'] = display_thang['Doanh thu'].apply(lambda x: f"{x:,.0f}")
    display_thang['Lãi gộp'] = display_thang['Lãi gộp'].apply(lambda x: f"{x:,.0f}")
    
    st.dataframe(display_thang, use_container_width=True, hide_index=True)

# ==================== DASHBOARD 4: KẾ HOẠCH 2026 ====================
elif dashboard_option == "🎯 Kế hoạch 2026":
    st.title("🎯 Kế hoạch 2026")
    
    # Mục tiêu chính
    st.subheader("🎯 Mục tiêu chính năm 2026")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="💰 Doanh thu",
            value="157.4 tỷ",
            delta="+12% vs 2025"
        )
    
    with col2:
        st.metric(
            label="💵 Lãi gộp",
            value="28.0 tỷ",
            delta="+9% vs 2025"
        )
    
    with col3:
        st.metric(
            label="📊 Lãi trước thuế",
            value="4.19 tỷ",
            delta="+35% vs 2025"
        )
    
    st.markdown("---")
    
    # Bullet chart
    st.subheader("🎯 Mục tiêu 2026 vs Thực hiện 2025")
    
    metrics = [
        {'title': 'Doanh thu', 'actual': 140.5, 'target': 157.4, 'max': 180},
        {'title': 'Lãi gộp', 'actual': 25.6, 'target': 28.0, 'max': 35},
        {'title': 'Lãi trước thuế', 'actual': 3.1, 'target': 4.19, 'max': 6}
    ]
    
    for metric in metrics:
        fig_bullet = go.Figure()
        
        # Vùng nền
        fig_bullet.add_trace(go.Bar(
            x=[metric['max']],
            y=[metric['title']],
            orientation='h',
            marker=dict(color='rgba(200, 200, 200, 0.3)'),
            name='Tối đa',
            showlegend=False
        ))
        
        # Vùng mục tiêu
        fig_bullet.add_trace(go.Bar(
            x=[metric['target']],
            y=[metric['title']],
            orientation='h',
            marker=dict(color='rgba(52, 152, 219, 0.5)'),
            name='Mục tiêu',
            showlegend=False
        ))
        
        # Thực tế
        fig_bullet.add_trace(go.Bar(
            x=[metric['actual']],
            y=[metric['title']],
            orientation='h',
            marker=dict(color='#e74c3c'),
            name='Thực hiện 2025',
            showlegend=False
        ))
        
        # Marker mục tiêu
        fig_bullet.add_trace(go.Scatter(
            x=[metric['target']],
            y=[metric['title']],
            mode='markers',
            marker=dict(color='black', size=15, symbol='line-ns-open'),
            name='KH 2026',
            showlegend=False
        ))
        
        fig_bullet.update_layout(
            height=100,
            barmode='overlay',
            xaxis=dict(title='Tỷ đồng'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig_bullet, use_container_width=True)
    
    st.markdown("---")
    
    # Tăng trưởng theo khối
    st.subheader("📈 Tăng trưởng dự kiến theo Khối")
    
    fig_growth_khoi = go.Figure()
    
    x = data_khoi['Khối']
    
    fig_growth_khoi.add_trace(go.Bar(
        name='TH 2025',
        x=x,
        y=data_khoi['TH 2025'],
        marker_color='#f39c12',
        text=[f"{v:,.0f}" for v in data_khoi['TH 2025']],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>TH 2025: %{y:,.0f} triệu<extra></extra>'
    ))
    
    fig_growth_khoi.add_trace(go.Bar(
        name='KH 2026',
        x=x,
        y=data_khoi['KH 2026'],
        marker_color='#2ecc71',
        text=[f"{v:,.0f}" for v in data_khoi['KH 2026']],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>KH 2026: %{y:,.0f} triệu<extra></extra>'
    ))
    
    # Tính % tăng trưởng
    growth_pct = ((data_khoi['KH 2026'] - data_khoi['TH 2025']) / data_khoi['TH 2025'] * 100).round(1)
    
    # Thêm annotation
    for i, (khoi, pct) in enumerate(zip(x, growth_pct)):
        fig_growth_khoi.add_annotation(
            x=i,
            y=data_khoi['KH 2026'].iloc[i] + 5000,
            text=f"+{pct}%",
            showarrow=False,
            font=dict(size=14, color='green' if pct > 0 else 'red', weight='bold')
        )
    
    fig_growth_khoi.update_layout(
        height=500,
        yaxis_title="Triệu đồng",
        barmode='group',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig_growth_khoi, use_container_width=True)
    
    # Highlight
    st.success("🚀 **Điểm nhấn**: Khối TMĐT dự kiến tăng trưởng đột phá **+98%**, từ 3.5 tỷ lên 7.0 tỷ")

# ==================== DASHBOARD 5: PHÂN TÍCH SẢN PHẨM ====================
elif dashboard_option == "📦 Phân tích sản phẩm":
    st.title("📦 Phân tích Sản phẩm")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🌳 Treemap - Doanh thu theo nhóm sản phẩm")
        
        fig_treemap = px.treemap(
            data_sanpham,
            path=['Nhóm sản phẩm'],
            values='Doanh thu',
            color='Doanh thu',
            color_continuous_scale='Blues',
            hover_data={'Tỷ trọng': ':.1f'}
        )
        
        fig_treemap.update_traces(
            textinfo="label+value+percent parent",
            texttemplate="<b>%{label}</b><br>%{value:,.0f} triệu<br>%{percentParent:.1%}"
        )
        
        fig_treemap.update_layout(height=500)
        
        st.plotly_chart(fig_treemap, use_container_width=True)
    
    with col2:
        st.subheader("📊 Tỷ trọng sản phẩm")
        
        fig_pie_sp = px.pie(
            data_sanpham,
            values='Doanh thu',
            names='Nhóm sản phẩm',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        
        fig_pie_sp.update_traces(textposition='inside', textinfo='percent')
        fig_pie_sp.update_layout(height=500)
        
        st.plotly_chart(fig_pie_sp, use_container_width=True)
    
    st.markdown("---")
    
    # Top 10 sản phẩm (giả lập)
    st.subheader("🏆 Top 10 Sản phẩm bán chạy")
    
    top10_data = pd.DataFrame({
        'Sản phẩm': [f'Sản phẩm {i}' for i in range(1, 11)],
        'Số lượng': np.random.randint(500, 2000, 10),
        'Doanh thu (triệu)': np.random.randint(5000, 15000, 10),
        'Lãi gộp (triệu)': np.random.randint(1000, 4000, 10)
    })
    
    top10_data = top10_data.sort_values('Doanh thu (triệu)', ascending=False)
    
    # Tạo heatmap style
    def color_scale(val, min_val, max_val):
        normalized = (val - min_val) / (max_val - min_val)
        return f'background-color: rgba(52, 152, 219, {normalized})'
    
    st.dataframe(
        top10_data.style.background_gradient(subset=['Doanh thu (triệu)'], cmap='Blues'),
        use_container_width=True,
        hide_index=True
    )

# ==================== DASHBOARD 6: PHÂN TÍCH KHÁCH HÀNG ====================
elif dashboard_option == "👥 Phân tích khách hàng":
    st.title("👥 Phân tích Khách hàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🍩 Doanh thu theo phân khúc")
        
        fig_kh_donut = px.pie(
            data_khachhang,
            values='Doanh thu',
            names='Phân khúc',
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig_kh_donut.update_traces(
            textposition='outside',
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Doanh thu: %{value:,.0f} triệu<br>Tỷ trọng: %{percent}<extra></extra>'
        )
        
        fig_kh_donut.update_layout(height=500)
        
        st.plotly_chart(fig_kh_donut, use_container_width=True)
    
    with col2:
        st.subheader("📊 So sánh phân khúc")
        
        fig_kh_bar = px.bar(
            data_khachhang.sort_values('Doanh thu', ascending=True),
            y='Phân khúc',
            x='Doanh thu',
            orientation='h',
            text='Doanh thu',
            color='Doanh thu',
            color_continuous_scale='Viridis'
        )
        
        fig_kh_bar.update_traces(
            texttemplate='%{text:,.0f}',
            textposition='outside'
        )
        
        fig_kh_bar.update_layout(
            height=500,
            xaxis_title="Doanh thu (triệu đồng)",
            showlegend=False
        )
        
        st.plotly_chart(fig_kh_bar, use_container_width=True)
    
    st.markdown("---")
    
    # Top 20 khách hàng (giả lập)
    st.subheader("🏆 Top 20 Khách hàng VIP")
    
    top20_kh = pd.DataFrame({
        'Khách hàng': [f'Khách hàng {i}' for i in range(1, 21)],
        'Doanh thu 2025 (triệu)': np.random.randint(2000, 8000, 20),
        'Tăng trưởng (%)': np.random.randint(-10, 50, 20),
        'Tình trạng': np.random.choice(['Tốt', 'Bình thường', 'Cần chú ý'], 20)
    })
    
    top20_kh = top20_kh.sort_values('Doanh thu 2025 (triệu)', ascending=False)
    
    # Color coding
    def color_status(val):
        if val == 'Tốt':
            return 'background-color: #d4edda'
        elif val == 'Bình thường':
            return 'background-color: #fff3cd'
        else:
            return 'background-color: #f8d7da'
    
    st.dataframe(
        top20_kh.style.applymap(color_status, subset=['Tình trạng']),
        use_container_width=True,
        hide_index=True
    )

# ==================== DASHBOARD 7: TÀI CHÍNH ====================
elif dashboard_option == "💰 Tài chính":
    st.title("💰 Phân tích Tài chính")
    
    # Waterfall chart - Từ doanh thu đến lãi ròng
    st.subheader("💧 Waterfall: Từ Doanh thu đến Lãi ròng")
    
    waterfall_data = {
        'measure': ['absolute', 'relative', 'relative', 'relative', 'relative', 'total'],
        'x': ['Doanh thu', 'Giá vốn', 'Chi phí logistics', 'Chi phí nhân sự', 'Chi phí khác', 'Lãi ròng'],
        'y': [140541, -114931, -8000, -7500, -7000, 3110]
    }
    
    fig_waterfall = go.Figure(go.Waterfall(
        measure=waterfall_data['measure'],
        x=waterfall_data['x'],
        y=waterfall_data['y'],
        text=[f"{abs(v):,.0f}" for v in waterfall_data['y']],
        textposition='outside',
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#e74c3c"}},
        increasing={"marker": {"color": "#2ecc71"}},
        totals={"marker": {"color": "#3498db"}}
    ))
    
    fig_waterfall.update_layout(
        height=500,
        yaxis_title="Triệu đồng",
        showlegend=False
    )
    
    st.plotly_chart(fig_waterfall, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart cơ cấu chi phí
        st.subheader("🥧 Cơ cấu Chi phí")
        
        chiphi_data = pd.DataFrame({
            'Loại chi phí': ['Giá vốn', 'Logistics', 'Nhân sự', 'Marketing', 'Chênh lệch tỷ giá', 'Khác'],
            'Giá trị': [114931, 8000, 7500, 3000, 1000, 2000]
        })
        
        fig_chiphi = px.pie(
            chiphi_data,
            values='Giá trị',
            names='Loại chi phí',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Reds_r
        )
        
        fig_chiphi.update_traces(textposition='inside', textinfo='percent+label')
        fig_chiphi.update_layout(height=400)
        
        st.plotly_chart(fig_chiphi, use_container_width=True)
    
    with col2:
        # Tỷ suất lợi nhuận
        st.subheader("📈 Tỷ suất Lợi nhuận")
        
        ty_suat_data = pd.DataFrame({
            'Chỉ tiêu': ['Tỷ suất lãi gộp', 'Tỷ suất lãi ròng'],
            '2024': [20.0, 2.5],
            '2025': [18.2, 2.2],
            '2026 (KH)': [17.8, 2.7]
        })
        
        fig_ty_suat = go.Figure()
        
        for chi_tieu in ty_suat_data['Chỉ tiêu']:
            row = ty_suat_data[ty_suat_data['Chỉ tiêu'] == chi_tieu]
            fig_ty_suat.add_trace(go.Scatter(
                x=['2024', '2025', '2026 (KH)'],
                y=[row['2024'].values[0], row['2025'].values[0], row['2026 (KH)'].values[0]],
                name=chi_tieu,
                mode='lines+markers',
                line=dict(width=3),
                marker=dict(size=10)
            ))
        
        fig_ty_suat.update_layout(
            height=400,
            yaxis_title="Phần trăm (%)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig_ty_suat, use_container_width=True)
    
    st.markdown("---")
    
    # KPI tài chính
    st.subheader("📊 Chỉ số Tài chính chính")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tỷ suất lãi gộp", "18.2%", "-1.8%")
    
    with col2:
        st.metric("Tỷ suất lãi ròng", "2.2%", "-0.3%")
    
    with col3:
        st.metric("ROE (ước tính)", "12.5%", "+1.2%")
    
    with col4:
        st.metric("Vòng quay hàng tồn kho", "4.2 lần/năm", "-0.3")

# ==================== DASHBOARD 8: EXECUTIVE SUMMARY ====================
elif dashboard_option == "🎬 Executive Summary":
    st.title("🎬 Executive Summary - Báo cáo Điều hành")
    
    st.markdown("### 📅 Tháng " + datetime.now().strftime("%m/%Y"))
    
    # KPI Cards lớn
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <h3>💰 Doanh thu</h3>
                <h1>140.5 tỷ</h1>
                <p>89% KH | -11%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <h3>💵 Lãi gộp</h3>
                <h1>25.6 tỷ</h1>
                <p>88% KH | -12%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-card">
                <h3>📊 Lãi trước thuế</h3>
                <h1>3.1 tỷ</h1>
                <p>65% KH | -35%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="metric-card">
                <h3>🎯 Đạt KH</h3>
                <h1>89%</h1>
                <p>Cần cải thiện</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sparklines
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Xu hướng Doanh thu 12 tháng")
        
        sparkline_data = data_thang_2026['Doanh thu'].tolist()
        
        fig_spark = go.Figure()
        fig_spark.add_trace(go.Scatter(
            y=sparkline_data,
            mode='lines',
            line=dict(color='#3498db', width=2),
            fill='tozeroy',
            fillcolor='rgba(52, 152, 219, 0.2)'
        ))
        
        fig_spark.update_layout(
            height=150,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_spark, use_container_width=True)
    
    with col2:
        st.subheader("📊 Xu hướng Lãi gộp 12 tháng")
        
        sparkline_data2 = data_thang_2026['Lãi gộp'].tolist()
        
        fig_spark2 = go.Figure()
        fig_spark2.add_trace(go.Scatter(
            y=sparkline_data2,
            mode='lines',
            line=dict(color='#2ecc71', width=2),
            fill='tozeroy',
            fillcolor='rgba(46, 204, 113, 0.2)'
        ))
        
        fig_spark2.update_layout(
            height=150,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig_spark2, use_container_width=True)
    
    st.markdown("---")
    
    # Traffic lights
    st.subheader("🚦 Tình trạng các chỉ tiêu")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Doanh thu**")
        st.markdown("🟡 Cảnh báo")
        st.caption("89% KH")
    
    with col2:
        st.markdown("**Lãi gộp**")
        st.markdown("🟡 Cảnh báo")
        st.caption("88% KH")
    
    with col3:
        st.markdown("**Tồn kho**")
        st.markdown("🟢 Tốt")
        st.caption("Trong kiểm soát")
    
    with col4:
        st.markdown("**Cash Flow**")
        st.markdown("🟢 Tốt")
        st.caption("Ổn định")
    
    st.markdown("---")
    
    # Cảnh báo & Hành động
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚠️ Cảnh báo cần chú ý")
        st.error("🔴 Ban Học liệu chỉ đạt 58% KH")
        st.warning("🟡 Chi phí chênh lệch tỷ giá tăng 1 tỷ")
        st.warning("🟡 Tỷ suất lãi gộp giảm 1.8% so với 2024")
    
    with col2:
        st.subheader("✅ Điểm sáng")
        st.success("🟢 Ban PT & TTNN đạt 100% KH")
        st.success("🟢 Ban KD TM & DV đạt 100% KH")
        st.success("🟢 Khối TMĐT vượt KH (101%)")
    
    st.markdown("---")
    
    # Khuyến nghị
    st.subheader("💡 Khuyến nghị hành động")
    
    st.info("""
    **Ưu tiên cao:**
    1. Tập trung hỗ trợ Ban Học liệu đạt KH 2026 (tăng 125%)
    2. Kiểm soát rủi ro tỷ giá, xem xét hedging cho các đơn hàng lớn
    3. Đẩy mạnh đầu tư vào Khối TMĐT để đạt mục tiêu tăng trưởng 98%
    
    **Trung hạn:**
    4. Hoàn thiện triển khai ERP trong Q1/2026
    5. Xây dựng đề án Trung tâm Phim ảnh
    6. Tối ưu cơ cấu chi phí để cải thiện tỷ suất lãi
    """)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>📊 CDIMEX Dashboard | Phát triển bởi R&D Team | 
        <a href='mailto:thuong@vietravel.com'>thuong@vietravel.com</a></p>
    </div>
""", unsafe_allow_html=True)
