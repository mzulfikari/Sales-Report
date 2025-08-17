from django.core.validators import RegexValidator

iran_plaque_validator = RegexValidator(
    regex=r'^[0-9]{2}[آ-یA-Z]{1}[0-9]{3,4}$',
    message="شماره پلاک باید شامل دو رقم، یک حرف فارسی یا انگلیسی و سه یا چهار رقم باشد. مثال: 12ب345 یا 12A6789"
)