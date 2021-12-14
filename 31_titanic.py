import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('titanic_data/train.csv')
	print(data.count())
	print(data.head())
	# 製造畫布
	plt.figure(figsize=(18, 7))
	# 切割
	plt.subplot2grid((3, 4), (0, 0))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	# kind='bar'畫出直條圖 or kind='pie'
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 2))
	# kind='bar'畫出直條圖 or kind='pie
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (1, 0))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Man Survived')

	plt.subplot2grid((3, 4), (1, 1))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('woman Survived')

	plt.subplot2grid((3, 4), (2, 0))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[(data.Sex == 'male') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='magenta')
	plt.title('Rich Man Survived')

	plt.subplot2grid((3, 4), (2, 1))
	# kind='bar'畫出直條圖 or kind='pie
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[(data.Sex == 'male') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar',																				color='magenta')
	plt.title('Poor Man Survived')

	plt.subplot2grid((3, 4), (2, 2))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[(data.Sex == 'female') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Rich Woman Survived')

	plt.subplot2grid((3, 4), (2, 3))
	# kind='bar'畫出直條圖 or kind='pie
	data.Survived[(data.Sex == 'female') & (data.Pclass == 3)].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Poor Woman Survived')


	plt.show()


if __name__ == '__main__':
	main()
