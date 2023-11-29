class Cat:
    def mews(self):
        print('meow!')
#Lionクラスは、Catクラスのすべてのメソッドと属性を継承している
class Lion(Cat):
    def bark(self):
        print('raaar!')

leo=Lion()
leo.mews()
#meow!と出る(継承)
"""継承を利用することで、親クラスの機能や属性を引き継ぎながら、
子クラスに独自の機能や属性を追加することができる"""