from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class MedicationCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = 'MedicationCategory'
        verbose_name_plural = 'MedicationCategories'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Поставщик')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, verbose_name='Телефонный номер')

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название филлиала аптеки')
    location = models.CharField(max_length=200, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Место работы')
    photo = models.ImageField(upload_to="photos", blank=True)
    description = models.TextField(blank=True, verbose_name='Описание выполняемых работ')
    phone_number = models.CharField(max_length=20, verbose_name='Телефонный номер', null=True)
    email = models.CharField(max_length=20, verbose_name='Почта', null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return f"Employee{self.id}"


class Medication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название лекарства')
    content = models.TextField(blank=True, verbose_name='Описание лекарства')
    #photo = models.ImageField(upload_to="photos/%Y/%n/%d/", null=True)
    category = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE, verbose_name='Категория препарата')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(verbose_name='Количество доступных')
    is_available = models.BooleanField(default=True, verbose_name='Есть ли в продаже')

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bying', kwargs={'bying_id': self.pk})

    def get_absolute_url1(self):
        return reverse('thanks', kwargs={'thanks_id': self.pk})


class Sale(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, verbose_name='Продаваемое лекарство')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Продавец')
    quantity = models.PositiveIntegerField(verbose_name='Количество проданных')
    date = models.DateField(auto_now_add=True, verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return f"{self.medication.title} - {self.employee.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(max_length=20, verbose_name='Телефонный номер')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, verbose_name='Лекарство')

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


class Coupon(models.Model):
    archived = models.BooleanField(default=True, verbose_name='Архив')
    title = models.CharField(max_length=100, verbose_name='Название купона')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    date = models.DateField(auto_now_add=True, verbose_name='Дата добавления на сайт')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание вакансии')
    salary = models.PositiveIntegerField(verbose_name='Предлагаемая зарплата')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Клиент')
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    rating = models.IntegerField(validators=[
            MinValueValidator(0, message='Рейтинг должен быть не меньше 0.'),
            MaxValueValidator(5, message='Рейтинг должен быть не больше 5.'),
        ], verbose_name='Рейтинг')
    feedback = models.TextField(blank=True, null=True, verbose_name='Отзыв')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


class News(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    summary = models.TextField(blank=True, verbose_name='Краткое содержание')
    article = models.TextField(blank=True, verbose_name='Вся статья')
    image = models.ImageField(upload_to="static/medicines/images/news", blank=True)



