from django.db import models
from stdimage.models import StdImageField
import uuid


# uuid.uuid4() - gera um nome aleatório, substituindo no nome recebido. Manteremos a extensão
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# tabela de Equipe
# quando utiliza foreign key nas classes, utilizar o on_delete.
# vai criar um diretorio midia e um diretorio team e jogar essas imagens lá.
# #Crop é em caso de necessidade, corta a imagem
# get_file_path é utilizado aqui para cirar o arquivo que subiu, mas renomeado e garantindo unicidade
class Team(Base):
    name = models.CharField('Name', max_length=100)
    bio = models.TextField('Bio', max_length=140)
    image = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name


class Testemonial(Base):
    nome = models.CharField('Nome', max_length=100)
    image = StdImageField('Imagem', upload_to=get_file_path,
                          variations={'thumb': {'width': 48, 'height': 48, 'crop': True}})
    bairro = models.CharField('bairro', max_length=50)
    texto = models.TextField('Depoimento', max_length=500)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome
