from django import forms #django内のformsメソッドをインポートする
from .models import Day #diaryフォルダ内のmodels.pyのクラスDayを呼び出す


class DayCreateForm(forms.ModelForm): #formsクラスのModelFormメソッドを使う(継承)。
    """ModelFormはあらゆる起こりうるエラーやインプットなどの記載しなければいけないことを
            簡易的にしてくれるメソッドアイテム
            この場合Dayクラスに記載している内容から自動的に処理をしてくれる
            formメソッドを継承する場合にはformに記載していかなければならない"""

    class Meta:
        model = Day #class Dayをmodel変数に代入　←　対象
        """Dayをもとにモデルを作成する"""
        fields = '__all__'
        """どこのフィールド(title, text, dateなど)"""
