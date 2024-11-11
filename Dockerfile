# ���������� ����� Python 3.9
FROM python:3.9-slim

# ������������� ������� ����������
WORKDIR /app

# �������� ���� ������������ � ���������
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# �������� ��� ����� ������� � ���������
COPY . /app/

# ��������� ���� 8000 ��� ������� � ���������� Django
EXPOSE 8000

# ������� ��� ������� ������� Django ��� ������ ����������
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
 
