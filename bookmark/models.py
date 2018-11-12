from django.db import models

# Create your models here.
# 모델을 작성
# 모델 : 데이터베이스의 묘사 - 어떤 테이블을 만들 것인지, 어떤 컬럼을 만들 것인지, 어떤 제약 조건을 둘것인지

# models.Model
# 장고에서 모델은 ORM(Object-relational mapping)이란 기능을 통해서 프로그래머가 SQL을 몰라도 데이터베이스를 사용할 수 있도록 도와줍니다.
# models.Model이 실제적인 기능 함수를 가지고 있다.

# 모델까지 만들었을 경우 : 아직 DB에 반영이 안된 상태
# makemigrations, migrate
# python manage.py makemigrations bookmark

# python manage.py sqlmigrate bookmark 0001

# python manage.py migrate bookmark 0001

# 데이터베이스에 직접 접근하는 방법 : python manage.py dbshell

# 데이터베이스에 간접적으로 접근하는 방법(모델을 이용해서) : python manage.py shell


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def __str__(self):  # 객체를 출력할 때, 나타내는 값
        return self.site_name + ", 주소 : " + self.url

    # 모델 내부의 메소드들은 필드처럼 사용될 수 있다
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id)])

    class Meta:
        ordering = ['site_name']
