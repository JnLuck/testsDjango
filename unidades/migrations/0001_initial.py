# Generated by Django 4.2 on 2023-10-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(choices=[('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9')], max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(choices=[('Modulo 1', 'Modulo 1'), ('Modulo 2', 'Modulo 2'), ('Modulo 3', 'Modulo 3')], max_length=50)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCompetencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUnidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDidactica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('horas', models.IntegerField()),
                ('ciclo', models.IntegerField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.modulo')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.plan')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.tipounidad')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('capacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.indicador')),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(choices=[('UC1', 'UC1'), ('UC2', 'UC2'), ('UC3', 'UC3'), ('UC4', 'UC4'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CE3', 'CE3'), ('CE4', 'CE4')], max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.tipocompetencia')),
                ('unidad_didactica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidaddidactica')),
            ],
        ),
        migrations.AddField(
            model_name='capacidad',
            name='competencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.competencia'),
        ),
    ]
