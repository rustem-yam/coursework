# coursework

## Нововведения с прошлого семестра

### API View (DRF)

В api/views.py реализовано несколько представлений для моделей Post, Comment и Likes
В users/views.py реализовано несколько представлений для моделей CustomUser и Friend

### Запросы с Q

В messages/views.py для представления чата были использованы запросы с Q и логическим оператором ИЛИ
В users/views.py для представления моделей Friend были использованы запросы с Q и логическими операторами И, ИЛИ и НЕ

### Пагинация

В users/views.py для представления списка пользователей был использован модуль PageNumberPagination в рамках DRF
В api/views.py для представления списка комментариев был использован модуль Paginator в рамках Django

### Фильтрация (DRF)

В users/views.py для представления списка пользователей имеются фильтры DjangoFilterBackend, SearchFilter и OrderingFilter

### Сохранение истории изменений объектов (Django-Simple-History)

В message/models.py для модели сообщения добавлено отслеживание истории изменений

### Экспорт данных в эксель (Django-Import-Export)

В api/resources.py были созданы Resource для моделей Post и Comment. В ресурсе Comment используются кастомизированные методы dehydrate_full_title и after_export
В api.admin.py к Admin настройкам к моделям Comment и Post были указаны соответствующие resource, для PostAdmin реализован кастомный метод get_export_queryset

### Management команда

В api/management/commands/comment_export.py была реализована management команда для вывода в консоль CSV-формат эскпорта комментариев

### Валидация полей

В api/serializers.py для сериализатора создания поста была добавлена валидация текста, пресекающая использование запрещённого слова
В users/serializers.py для сериализатора регистрации пользователя была добавления валидация имени, пресекающая использование слишком длинного имени

### Миксин @action для ViewSet

В api/views.py создан ViewSet для постов с представлениями для получения списка поста с миксином @action(methods=['GET'], detail=False) и для удаления поста с миксинов @action(methods=["POST"], detail=True)

### Настройка админки

В message/admin.py для регистрации модели Message использованы настройки fieldsets, date_hierarchy, list_display, list_filter, search_fields и raw_id_fields
В api/admin.py были использованы схожие настройки, а также inlines
В users/admin.py были использованы схожие настройки, а также add_fieldsets и ordering
