# -*- coding: utf-8 -*-
"""Integral2_LuanaTomazAccorsi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V_FOOQGTygc3AOj8D3MHB04-YCMbxOd9
"""

#Realizado por Luana Tomaz Accorsi
#e-mail: luana.tomaza@gmail.com

from manim import *

class IntegralArea(Scene):
    def construct(self):
       #definiçao de função que retorna uma linha vertical entre duas funções function1 e function2 e os dois pontos de interseção entre essa reta e as curvas.
        def get_vertical_line_to_graph(axes, function1, function2, x, width, color):
            result=VGroup()
            line = Line(
                start=axes.c2p(x, function1.underlying_function(x)),
                end=axes.c2p(x, function2.underlying_function(x)),
                stroke_width=width,
                stroke_color=color,
            )
            dot1=Dot().set_color(color).move_to(axes.c2p(x, function1.underlying_function(x)))
            dot2=Dot().set_color(color).move_to(axes.c2p(x, function2.underlying_function(x)))
            result.add(line, dot1, dot2)
            return result




    #criacao dos eixos
        eixos = Axes(
            #intervalo dos eixos
            x_range=[-3,3],
            y_range=[-1,5],
            #inclusão dos números visualmente
            x_axis_config={"numbers_to_include":(-2,2),"font_size":50},
            y_axis_config={"numbers_to_include":(2,4),"font_size":50}
        )

        labels = eixos.get_axis_labels()

        #colocação da equação
        curve_1_0 = eixos.plot(lambda x: x,x_range=[-3,3],color=GREEN)
        curve_1_1 = eixos.plot(lambda x: -x,x_range=[-2.75,3],color=GREEN)
        curve_1 = eixos.plot(lambda x: -x+2,x_range=[-3,3],color=YELLOW)


        #colocação da equação
        curve_2_0=eixos.plot(lambda x: x**2,x_range=[-2.3,2.3],color=GREEN)
        curve_2_1=eixos.plot(lambda x: -x**2,x_range=[-3,3],color=GREEN)
        curve_2 = eixos.plot(
            lambda x: -x ** 2 +4,
            x_range=[-2.5,2.5],
            color=ORANGE,
        )



        #ponto
        ponto = Dot().move_to(eixos.c2p(-1, 3))
        ponto1 = Dot().move_to(eixos.c2p(2, 0))
        ponto_A = MathTex(r"a",color = WHITE,font_size=60).move_to(point_or_mobject=[-2,1.5,0])
        ponto_B = MathTex(r"b",color = WHITE,font_size=60).move_to(point_or_mobject=[4.2,-1.6,0])
        ponto_x1 = MathTex(r"-1",color = WHITE,font_size=30).move_to(point_or_mobject=[-4.77,-1.65,0])
        ponto_x2 = MathTex(r"2",color = WHITE,font_size=30).move_to(point_or_mobject=[-1.01,-1.6,0])





        #marcando a área
        area1 = eixos.get_area(curve_1, [-1, 2], bounded_graph=curve_2, color=PURPLE, opacity=0.5)

        #parte texto
        f_1=MathTex(r" -x+2", color = YELLOW,font_size=70).move_to(point_or_mobject=[-3.7,3.2,0])
        f= MathTex(r"-x+2", color = YELLOW,font_size=45).move_to(point_or_mobject=[-3.5,2.5,0])
        explic_curva0=MathTex(r" x", color=GREEN,font_size=45).move_to(point_or_mobject=[5,1,0])
        explic_curva1=MathTex(r"-x", color=GREEN,font_size=45).move_to(point_or_mobject=[-4.5,0.8,0])

        f_2= MathTex(r"-x^2 + 4", color = ORANGE,font_size=70).move_to(point_or_mobject=[3.7,1.6,0])
        f2= MathTex(r" -x^2 + 4", color = ORANGE,font_size=45).move_to(point_or_mobject=[2.7,2,0])
        explic_curva1_0=MathTex(r" x^2", color=GREEN,font_size=45).move_to(point_or_mobject=[3.5,2,0])
        explic_curva1_1=MathTex(r"-x^2",color=GREEN,font_size=45).move_to(point_or_mobject=[3,-3,0])




        explic=MathTex(
           r" \textrm{Abscissa de $a$ e $b$ :} ",font_size=45,color=RED
        ).move_to(point_or_mobject=[4.2,2,0])
        explic1=MathTex(
           r" g(x) \, = \, f(x) ",font_size=40
        ).move_to(point_or_mobject=[4,1,0])
        explic2=MathTex(
           r" -x+2=-x^2+4 ",font_size=40
        ).move_to(point_or_mobject=[4,0,0])
        explic3=MathTex(
           r" x^2-x-2=0 ",font_size=40
        ).move_to(point_or_mobject=[4,-1,0])
        explic4=MathTex(
           r" x_1 \, = -1 \, \, , \, \, x_2 \, = \, 2 ",font_size=40
        ).move_to(point_or_mobject=[4,-2,0])



        integ=MathTex(
           r" \textrm{Área:} ",font_size=45,color=RED
        ).move_to(point_or_mobject=[3.2,2.5,0])
        integral=MathTex(
           r" \int_{-1}^2 ", r" ( \,", r" f(x) \, ", r"- \, ", r" g(x) \,", r" ) \, ",r" dx \, = ",font_size=40
        ).move_to(point_or_mobject=[3,1.5,0])
        int1=MathTex(
           r" \int_{-1}^2  ( \,", r" -x^2+4 \, ", r" - \,  ", r"  (", r"-x+2", r") ", r" \, ) \, ", r" dx\, =", font_size=40
        ).move_to(point_or_mobject=[4,0,0])

        inte=MathTex(
           r" \bigg (\frac{-x^3}{3} \, + \, \frac{x^2}{2}  \, + 2 \, x  \bigg )  \bigg \arrowvert_{-1}^{2} \, = \,", r" \, \, \frac{9}{2}",font_size=40
        ).move_to(point_or_mobject=[4,0,0])

        integral2=MathTex(
           r" \int_{-1}^2  ( \, -x^2+x+2 \, )\, dx = ",font_size=40
        ).move_to(point_or_mobject=[4,0,0])



        inicio=MathTex(r"\textrm{Determine o valor da área definida entre as curvas} \,",font_size=45).move_to(point_or_mobject=[0,1,0])
        inicio_1=MathTex(r" g(x) \, = \,-x+2  \, \, \,  \textrm{e}\, \, \, f(x) \, = \, -x^2+4. \, \,",font_size=45).move_to(point_or_mobject=[0,0,0])
        inicio2=MathTex(r"\textrm{A área definida entre as curvas} \,  g(x) \, = \,-x+2 \, \,  \textrm{e} \, \,  f(x) \, = \, -x^2+4. \, \, \,",font_size=37).move_to(point_or_mobject=[0,3.65,0])
        inicio2_1=MathTex(r"\textrm{A área definida entre as curvas} \,  g(x) \, = \,-x+2 \, \,  \textrm{e} \, \,  f(x) \, = \, -x^2+4. \, \, \,",font_size=37).move_to(point_or_mobject=[0,3.35,0])



        #grupo
        vg=VGroup(eixos,labels,curve_1,f_1,curve_2,f_2,area1,ponto,ponto1,ponto_A,ponto_B)
        ajuda=VGroup(integral,int1,integral2,inte)
        ajuda.arrange(1.3*DOWN,center=False, aligned_edge=LEFT)



        #adicionando
        self.add(inicio, inicio_1)
        self.wait(3)
        self.play(FadeOut(inicio,inicio_1))
        self.add(inicio2,eixos, labels)
        self.wait(1)
        self.add(curve_1_0,explic_curva0)
        self.wait(2)
        self.play(ReplacementTransform(curve_1_0,curve_1_1),ReplacementTransform(explic_curva0,explic_curva1))
        self.wait(2)
        self.play(ReplacementTransform(curve_1_1, curve_1),ReplacementTransform(explic_curva1,f))
        self.wait(2)
        self.add(curve_2_0,explic_curva1_0)
        self.wait(2)
        self.play(ReplacementTransform(curve_2_0, curve_2_1),ReplacementTransform(explic_curva1_0,explic_curva1_1))
        self.wait(2)
        self.play(ReplacementTransform(curve_2_1,curve_2),ReplacementTransform(explic_curva1_1,f2))
        self.wait(2)
        self.add(area1)
        self.wait(1)
#animação linha
        k = ValueTracker(-1)

        # definição da reta entre as curvas curve_1 e curve_2.
        moving_v_line = always_redraw(
            lambda: get_vertical_line_to_graph(
                axes=eixos, function1=curve_1, function2=curve_2, x=k.get_value(), width=4, color=GREEN
            )
        )

        self.play(FadeIn(moving_v_line)) # adicionar a reta na cena (somente essa linha não faz nada)
        self.play(k.animate.set_value(2), run_time=4, rate_func=smooth) #essa linha é a responsável pela animação, fazendo k variar de -1 definido acima até 0.
        self.play(FadeOut(moving_v_line)) #remove essa reta

        self.wait()
        self.play(FadeOut(f,f2))
        self.play(FadeOut(inicio2))
        self.add(inicio2_1)
        vg.shift(3.5*LEFT).height=4.5
        self.add(f_1,f_2)
        self.wait()
        self.add(explic)
        self.wait(1)
        self.add(ponto,ponto1,ponto_A,ponto_B)
        self.wait(1)
        self.play(Circumscribe(ponto_A, color=GREEN))
        self.wait(1)
        self.play(Circumscribe(ponto_B, color=GREEN))
        self.wait(1)
        self.play(Write(explic1))
        self.wait(3)
        self.play(Write(explic2))
        self.wait(3)
        self.play(Write(explic3))
        self.wait(3)
        self.play(Write(explic4))
        self.wait(3)
        self.add(ponto_x1,ponto_x2)
        self.play(Circumscribe(ponto_x2, color=GREEN))
        self.play(FadeOut(ponto_x2))
        self.play(Circumscribe(ponto_x1, color=GREEN))
        self.wait(5)
        self.play(FadeOut(explic,explic1,explic2,explic3,explic4))
        inte[1].set_color(LIGHT_PINK)
        self.add(integ)
        self.wait(1)
        self.play(Write(integral))
        self.wait(2)
        self.play(Write(int1[0]))
        self.play(Circumscribe(integral[2], color=ORANGE))
        self.play(Circumscribe(f_2),run_time=3)
        self.play(Write(int1[1]))
        self.wait(1)
        self.play(Write(int1[2]))
        self.play(Circumscribe(integral[4], color=YELLOW))
        self.play(Circumscribe(f_1))
        self.play(Write(int1[3]))
        self.play(Write(int1[4]))
        self.play(Write(int1[5]))
        self.wait()
        self.play(Write(int1[6]))
        self.play(Write(int1[7]))
        self.wait(1)
        self.play(Write(integral2))
        self.play(Write(inte))
        self.wait(3)