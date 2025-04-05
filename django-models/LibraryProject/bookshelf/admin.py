from django.contrib import admin
from .models import Book

# تخصيص واجهة الإدارة لموديل Book
class BookAdmin(admin.ModelAdmin):
    # تخصيص الأعمدة اللي هتظهر في القائمة الرئيسية
    list_display = ('title', 'author', 'publication_year')

    # إضافة فلاتر على الحقول لتسهيل البحث
    list_filter = ('author', 'publication_year')

    # إضافة خاصية البحث عن العناوين داخل واجهة الإدارة
    search_fields = ('title', 'author')

# تسجيل الموديل Book مع تخصيص واجهة الإدارة
admin.site.register(Book, BookAdmin)
