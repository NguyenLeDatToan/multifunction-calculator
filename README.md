# Máy tính đa chức năng (Python + Colab)

Liên kết Colab (chia sẻ công khai):

- https://colab.research.google.com/drive/1K7ohzXRq26N3gpw_hwRKUmGM-IuC1hOs?usp=sharing

## Tính năng

- Giải tỷ lệ: a/b = c/x → tìm x (trả về Fraction)
- Giải phương trình tìm x từ chuỗi (ví dụ: `2*x + 3 = 11`)
- Rút gọn/nhân căn bậc hai: `simplify_sqrt(n)`, `multiply_square_roots(a, b)`
- Chuyển đổi số thập phân ⇄ phân số ⇄ phần trăm

## Cấu trúc

- `calculator.py`: Thư viện hàm chính
- `multifunction_calculator.ipynb`: Notebook Colab có ví dụ và kiểm thử
- `requirements.txt`: Phụ thuộc `sympy`

## Hướng dẫn dùng nhanh (Local)

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python -i -c "import calculator as calc; print(calc.decimal_to_fraction_and_percent(0.125))"
```

## Dùng trên Google Colab

1. Mở liên kết Colab ở trên, hoặc mở notebook từ GitHub.
2. Chạy tuần tự các cell. Khi phần kiểm thử in ra “Tất cả kiểm thử đã PASSED!” là thành công.

## Bài kiểm tra/Submission

- Bật chia sẻ Colab: Anyone with the link → Viewer
- Gửi liên kết Colab (ở trên) để chấm.