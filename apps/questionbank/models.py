from django.db import models

from apps.account.models import UserModel
from apps.questionbank.enums import EducationLevelEnum, ExamTypeEnum, SubjectEnum, QuestionTypeEnum, \
    QuestionDifficultyLevelEnum
from apps.core.models import BaseModel

class EducationLevelModel(BaseModel):
    education_level = models.CharField(choices=EducationLevelEnum.choices(),max_length=50)

    def __str__(self):
        return self.education_level


    class Meta:
        db_table = 'education_level'

class ExamTypeModel(BaseModel):
    exam_type=models.CharField(choices=ExamTypeEnum.choices(),max_length=50)


    def __str__(self):
        return self.exam_type
    class Meta:
        db_table = 'exam_type'


class SubjectModel(BaseModel):
    subject_name=models.CharField(choices=SubjectEnum.choices(),max_length=50)

    def __str__(self):
        return self.subject_name
    class Meta:
        db_table = 'subject'

class ChapterModel(BaseModel):
    chapter_name=models.CharField(max_length=255,blank=False,null=False)
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.chapter_name
    class Meta:
        db_table = 'chapter'
        ordering = ['chapter_name']

class TopicModel(BaseModel):
    topic_name=models.CharField(max_length=255,blank=False,null=False)
    chapter = models.ForeignKey(ChapterModel,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.topic_name
    class Meta:
        db_table = 'topic'
        ordering = ['topic_name']

class TagModel(BaseModel):
    tag_name=models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.tag_name
    class Meta:
        db_table = 'tag'
        ordering = ['tag_name']

class QuestionModel(BaseModel):
    question=models.TextField(blank=False,null=True)
    question_type=models.CharField(choices=QuestionTypeEnum.choices(),max_length=50)
    marks=models.IntegerField(default=1)
    negative_marks=models.IntegerField(default=0)
    partial_marks=models.IntegerField(default=0)
    time=models.IntegerField(default=60)#in second
    difficulty_level=models.CharField(choices=QuestionDifficultyLevelEnum.choices(),max_length=50)
    explanation=models.TextField(blank=False,null=True)
    is_ai_generated = models.BooleanField(default=False)
    topic = models.ForeignKey(TopicModel,on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField(TagModel,blank=True,related_name='questions')
    added_by=models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,related_name='added_questions')
    verified_by=models.ForeignKey(UserModel,on_delete=models.SET_NULL,null=True,related_name='verified_questions')
    rating=models.IntegerField(default=0)

    def __str__(self):
        return self.question[:40] if self.question else ''
    class Meta:
        db_table = 'question'

class QuestionFileModel(BaseModel):
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    file=models.FileField(blank=False,null=False,upload_to='question_files')
    def __str__(self):
        return self.file.name
    class Meta:
        db_table = 'question_file'

class QuestionOptionModel(BaseModel):
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    option=models.TextField(blank=False,null=True)
    image=models.FileField(blank=False,null=False,upload_to='question_option_image')
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.option[:40] if self.option else ''
    class Meta:
        db_table = 'question_option'

class QuestionAnswerModel(BaseModel):
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    single_select_answer=models.ForeignKey(QuestionOptionModel,on_delete=models.SET_NULL,null=True,related_name="single_select_answer")
    multi_select_answer=models.ManyToManyField(QuestionOptionModel,blank=True,related_name="multi_select_answer")
    answer=models.TextField(blank=False,null=True)

    def __str__(self):
        return self.answer[:40] if self.answer else ''
    class Meta:
        db_table = 'question_answer'





