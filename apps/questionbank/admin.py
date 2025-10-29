from django.contrib import admin
from apps.questionbank.models import EducationLevelModel, ExamTypeModel, SubjectModel, ChapterModel, TopicModel, \
    TagModel, QuestionModel, QuestionOptionModel, QuestionFileModel, QuestionAnswerModel

admin.site.register(EducationLevelModel)
admin.site.register(ExamTypeModel)
admin.site.register(SubjectModel)
admin.site.register(ChapterModel)
admin.site.register(TopicModel)
admin.site.register(TagModel)
admin.site.register(QuestionModel)
admin.site.register(QuestionOptionModel)
admin.site.register(QuestionFileModel)
admin.site.register(QuestionAnswerModel)