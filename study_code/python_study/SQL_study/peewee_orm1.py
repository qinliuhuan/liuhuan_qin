from peewee import *

db = SqliteDatabase("sampleDB.db")


class BaseModel(Model):
    class Meta:
        database = db


class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField()
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'cursor'


class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=True)
    genger = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field="id", related_name="course")

    class Meta:
        order_by = ("name",)
        db_table = 'teacher'


'''operation the sql by ORM of before'''

Course.create_table()
Teacher.create_table()

Course.create(id=1, title='jingjixue', perion=320, description='wen li ke student can selcet to study')
Course.create(id=2, title='da xue English', period=300, description='da xue yi nianji ke xuanze')
Course.create(id=3, title='zhe xue', perion=100, description='bi xiu ke')
Course.create(id=104, title='bian yi yuan  li', period=100, description='ji suanji xitong xuanxiu ke')

Teacher.create(name='bai zhen jun', gender=True, address='sssss', course_id=1)
Teacher.create(name='li sen', gender=True, address='aaaaa', course_id=2)
Teacher.create(name='dai huanhuan', gender=False, address='ddddd', course_id=3)

# record = Course.get(Course.title = 'da xue English')
record = Course.get(title='da xue English')
print("course: %s, perion:%d" % (record.title, record.period))

record.period = 200
record.save()

record.delete_instance()

courses = Course.select()

courses = Course.select().where(Course.id < 10).order_by(Course.period.desc())

total = Course.select(fn.Avg(Course.period).alias('avg_period'))

Course.update(period=300).where(Course.id > 100).execute()

Record = Course.select().join(Teacher).where(genger = True)
