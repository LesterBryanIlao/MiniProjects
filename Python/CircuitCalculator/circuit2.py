from tkinter import *
from engineering_notation import *
from functools import partial
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import cmath
import tkinter.font as tkFont

def one(Frame):

    Frame.title("Example Curcuit 2")
    Frame.geometry("1360x750")

    bgImage = PhotoImage(file=r'CircuitTwo.PNG').subsample(2)
    Label(Frame, image=bgImage).place(relwidth=1, relheight=1.45)
    img = ImageTk.PhotoImage(Image.open("1.png"))
    Frame.wm_iconphoto(True, img)

    def call_result(label_Result, n1, n2, N1, N2, mult1, mult2):
        num1 = n1.get()
        num2 = n2.get()
        while (hasNumbers(str(num1))) or (hasNumbers(str(num2))) or (num1=='-0' and num2=='-0'):
            N1.delete(0, END)
            N2.delete(0, END)
            label_Result.delete(0, END)
            num1 = n1.get()
            num2 = n2.get()
            return num1, num2
        if (num1=='' and num2==''):
            pass
        elif (num2 == '0' or num2 == '' or num2 =='-0') and num1!='':
            num1 = EngNumber(float(num1) * translate(mult1.get()))
            result = str(num1)+' Ω'
        elif (num1 == '0' or num1 == '' or num1 =='-0') and num2!='':
            num1=0
            num2 = EngNumber(float(num2) * translate(mult2.get()))
            result = str(complex(num1,num2))+' Ω'
        else:
            num1 = float(num1) * translate(mult1.get())
            num2 = float(num2) * translate(mult2.get())
            if num2 > 0:
                result = str(EngNumber(num1))+'+'+str(EngNumber(num2)) + 'j Ω'
            elif num2 < 0:
                result = str(EngNumber(num1))+str(EngNumber(num2)) + 'j Ω'

        label_Result.delete(0, END)
        label_Result.insert(0, result)
        return

    # OUTPUT for Integer Numbers (Vsource)
    def call_resultVSource(label_Result, n, N, mult):
        num = n.get()
        while hasNumbers(str(num)):
            N.delete(0, END)
            label_Result.delete(0, END)
            num = n.get()
            return num
        num = str(EngNumber(float(num) * translate(mult.get()))) + 'V'
        label_Result.delete(0, END)
        label_Result.insert(0, num)
        return

    # OUTPUT for Integer Numbers (Csource)
    def call_resultCSource(label_Result, n, N, mult):
        num = n.get()
        while hasNumbers(str(num)):
            N.delete(0, END)
            label_Result.delete(0, END)
            num = n.get()
            return num
        num = str(EngNumber(float(num) * translate(mult.get()))) + 'A'
        label_Result.delete(0, END)
        label_Result.insert(0, num)
        return

    # Multiply() TRANSLATOR
    def translate(argument):
        switcher = {
            'G': 10 ** 9,
            'M': 10 ** 6,
            'K': 10 ** 3,
            ' ': 1,
            'select': 1,
            'm': 10 ** -3,
            'μ': 10 ** -6,
            'n': 10 ** -9,
        }
        return switcher.get(argument)

    # NUMBERS ONLY
    def hasNumbers(inputString):
        return any(char not in "-0123456789." for char in inputString)

    # MUTPLIER
    def Multiply():
        ops = ['G', 'M', 'K', ' ', 'm', 'μ', 'n']
        chosen = StringVar()
        chosen.set('select')
        multiplier = OptionMenu(Frame, chosen, *ops)
        return chosen, multiplier

    # Entry of Real and Imaginary
    def Entry_Re_Im():
        Re = StringVar()
        Im = StringVar()
        Real = Entry(Frame, width=25, borderwidth=3, textvariable=Re)
        Imag = Entry(Frame, width=25, borderwidth=3, textvariable=Im)
        return Re, Im, Real, Imag

    # Entry of Sources
    def Entry_Source():
        src = StringVar()
        Source = Entry(Frame, width=25, borderwidth=3, textvariable=src)
        return src, Source

    # ENTER VALUES BUTTON
    def EnterButton(func, result, _Re, _Im, _Real, _Imag, Chose1, Chose2):
        call_result = partial(func, result, _Re, _Im, _Real, _Imag, Chose1, Chose2)
        buttonCalc = Button(Frame, text="Enter Z1", width=6, borderwidth=3, command=call_result)
        return call_result, buttonCalc

    def EnterButtonSource(func, result, src, Source, chose):
        call_result = partial(func, result, src, Source, chose)
        buttonCalc = Button(Frame, text='Enter Source', width=10, borderwidth=3, command=call_result)
        return call_result, buttonCalc

    # MESH CURRENTS ANSWER


    def reset():
        Real1.delete(0, END)
        Imag1.delete(0, END)
        chosen1_1.set('select')
        chosen1_2.set('select')
        Real2.delete(0, END)
        Imag2.delete(0, END)
        chosen2_1.set('select')
        chosen2_2.set('select')
        Real3.delete(0, END)
        Imag3.delete(0, END)
        chosen3_1.set('select')
        chosen3_2.set('select')
        Real4.delete(0, END)
        Imag4.delete(0, END)
        chosen4_1.set('select')
        chosen4_2.set('select')
        Real5.delete(0, END)
        Imag5.delete(0, END)
        chosen5_1.set('select')
        chosen5_2.set('select')
        VoltSour.delete(0, END)
        chosen6_1.set('select')
        CurrSour.delete(0, END)
        chosen7_1.set('select')
        label_Result1.delete(0,END)
        label_Result2.delete(0,END)
        label_Result3.delete(0,END)
        label_Result4.delete(0,END)
        label_Result5.delete(0,END)
        label_Result6.delete(0,END)
        label_Result7.delete(0,END)
        Angle1.delete(0,END)
        Angle2.delete(0, END)
        Angle3.delete(0, END)
        Angle4.delete(0, END)
        Mesh_1.delete(0, END)
        Mesh_2.delete(0, END)
        Mesh_3.delete(0, END)
        Mesh_4.delete(0, END)


    def solve():
        def complexnumber():
            call_result(label_Result1, Re1, Im1, Real1, Imag1, chosen1_1, chosen1_2)
            call_result(label_Result2, Re2, Im2, Real2, Imag2, chosen2_1, chosen2_2)
            call_result(label_Result3, Re3, Im3, Real3, Imag3, chosen3_1, chosen3_2)
            call_result(label_Result4, Re4, Im4, Real4, Imag4, chosen4_1, chosen4_2)
            call_result(label_Result5, Re5, Im5, Real5, Imag5, chosen5_1, chosen5_2)
            call_resultVSource(label_Result6, Vsrc, VoltSour, chosen6_1)
            call_resultCSource(label_Result7, Csrc, CurrSour, chosen7_1)

        def output():
            def test(MeshCurr):
                if MeshCurr.imag == 0:
                    MeshCurr = str(EngNumber(MeshCurr.real)) + "A"
                elif MeshCurr.imag > 0:
                    MeshCurr = str(EngNumber(MeshCurr.real)) + "+" + str(EngNumber(MeshCurr.imag)) + 'j A'
                elif MeshCurr.imag < 0:
                    MeshCurr = str(EngNumber(MeshCurr.real)) + str(EngNumber(MeshCurr.imag)) + 'j A'
                return MeshCurr

            def blank(input):
                if input == '':
                    input = '0'
                return input

            a1_1 = float(blank(Real1.get())) * translate(blank(chosen1_1.get()))
            a1_2 = float(blank(Imag1.get())) * translate(blank(chosen1_2.get()))
            a = complex(a1_1, a1_2)
            b1_1 = float(blank(Real2.get())) * translate(blank(chosen2_1.get()))
            b1_2 = float(blank(Imag2.get())) * translate(blank(chosen2_2.get()))
            b = complex(b1_1, b1_2)
            c1_1 = float(blank(Real3.get())) * translate(blank(chosen3_1.get()))
            c1_2 = float(blank(Imag3.get())) * translate(blank(chosen3_2.get()))
            c = complex(c1_1, c1_2)
            d1_1 = float(blank(Real4.get())) * translate(blank(chosen4_1.get()))
            d1_2 = float(blank(Imag4.get())) * translate(blank(chosen4_2.get()))
            d = complex(d1_1, d1_2)
            e1_1 = float(blank(Real5.get())) * translate(blank(chosen5_1.get()))
            e1_2 = float(blank(Imag5.get())) * translate(blank(chosen5_2.get()))
            e = complex(e1_1, e1_2)
            V = float(VoltSour.get()) * translate(chosen6_1.get())
            C = float(CurrSour.get()) * translate(chosen7_1.get())
            num1 = np.array([[V, -d, 0, -a],
                             [0, 0, -c, a + b + c],
                             [0, d, c + e, -c],
                             [C, -1, 1, 0]])
            num2 = np.array([[a + d, V, 0, -a],
                             [-a, 0, -c, a + b + c],
                             [-d, 0, c + e, -c],
                             [0, C, 1, 0]])
            num3 = np.array([[a + d, -d, V, -a],
                             [-a, 0, 0, a + b + c],
                             [-d, d, 0, -c],
                             [0, -1, C, 0]])
            num4 = np.array([[a + d, -d, 0, V],
                             [-a, 0, -c, 0],
                             [-d, d, c + e, 0],
                             [0, -1, 1, C]])
            den = np.linalg.det(np.array([[a + d, -d, 0, -a],
                                          [-a, 0, -c, a + b + c],
                                          [-d, d, c + e, -c],
                                          [0, -1, 1, 0]]))

            MeshCurr1 = np.linalg.det(num1) / den
            MeshCurr2 = np.linalg.det(num2) / den
            MeshCurr3 = np.linalg.det(num3) / den
            MeshCurr4 = np.linalg.det(num4) / den
            phase1 = np.degrees(cmath.phase(MeshCurr1))
            phase2 = np.degrees(cmath.phase(MeshCurr2))
            phase3 = np.degrees(cmath.phase(MeshCurr3))
            phase4 = np.degrees(cmath.phase(MeshCurr4))
            Mesh_1.delete(0, END)
            Mesh_1.insert(0, test(MeshCurr1))
            Mesh_2.delete(0, END)
            Mesh_2.insert(0, test(MeshCurr2))
            Mesh_3.delete(0, END)
            Mesh_3.insert(0, test(MeshCurr3))
            Mesh_4.delete(0, END)
            Mesh_4.insert(0, test(MeshCurr4))
            Angle1.delete(0, END)
            Angle1.insert(0, str(round(abs(MeshCurr1), 2)) + u"\u2220" + str(round((phase1), 2)) + chr(176))
            Angle2.delete(0, END)
            Angle2.insert(0, str(round(abs(MeshCurr2), 2)) + u"\u2220" + str(round((phase2), 2)) + chr(176))
            Angle3.delete(0, END)
            Angle3.insert(0, str(round(abs(MeshCurr3), 2)) + u"\u2220" + str(round((phase3), 2)) + chr(176))
            Angle4.delete(0, END)
            Angle4.insert(0, str(round(abs(MeshCurr4), 2)) + u"\u2220" + str(round((phase4), 2)) + chr(176))

        def test(N1, N2):
            if hasNumbers(N1.get()) or hasNumbers(N2.get()) or (N1.get() == '-0' and N2.get() == '-0'):
                ans = 'fail'
            else: ans = 'pass'
            return ans

        def test1(N):
            if hasNumbers(N.get()) or N.get() == '-0':
                ans = 'fail'
            else:
                ans = 'pass'
            return ans

        Pass = (test(Re1, Im1) == 'pass' or test(Re2, Im2) == 'pass' or test(Re3, Im3) == 'pass'
                or test(Re4, Im4) == 'pass' or test(Re5, Im5) == 'pass' or test1(Vsrc) == 'pass' or test1(Csrc) == 'pass')
        Fail = (test(Re1, Im1) == 'fail' or test(Re5, Im5) == 'fail' or test(Re2, Im2) == 'fail' or test(Re3, Im3) == 'fail'
                or test(Re4, Im4) == 'fail' or test1(Vsrc) == 'fail' or test1(Csrc) == 'fail')
        if Fail:
            messagebox.showinfo("Error Notice", "Invalid values, try again.")
        if test(Re1, Im1) == 'fail':
            Real1.delete(0, END)
            Imag1.delete(0, END)
            chosen1_1.set('select')
            chosen1_2.set('select')
        elif test(Re2, Im2) == 'fail':
            Real2.delete(0, END)
            Imag2.delete(0, END)
            chosen2_1.set('select')
            chosen2_2.set('select')
        elif test(Re3, Im3) == 'fail':
            Real3.delete(0, END)
            Imag3.delete(0, END)
            chosen3_1.set('select')
            chosen3_2.set('select')
        elif test(Re4, Im4) == 'fail':
            Real4.delete(0, END)
            Imag4.delete(0, END)
            chosen4_1.set('select')
            chosen4_2.set('select')
        elif test(Re5, Im5) == 'fail':
            Real5.delete(0, END)
            Imag5.delete(0, END)
            chosen5_1.set('select')
            chosen5_2.set('select')
        elif test1(Csrc) == 'fail':
            CurrSour.delete(0, END)
            chosen7_1.set('select')
        elif test1(Vsrc) == 'fail':
            VoltSour.delete(0, END)
            chosen6_1.set('select')
        elif Pass:
            output()
            complexnumber()

    Label(Frame, text="Plug-in values.", font=('Helvetica',20)).grid(row=0, column=0)
    Label(Frame, text="Real (Re)").grid(row=1, column=1)
    Label(Frame, text="Imaginary (Im)").grid(row=1, column=3)
    Label(Frame, text="     ").grid(row=0, column=1)
    Label(Frame, text="     ").grid(row=0, column=2)
    Label(Frame, text="     ").grid(row=0, column=3)
    Label(Frame, text="     ").grid(row=0, column=4)
    Label(Frame, text="     ").grid(row=0, column=5)
    Label(Frame, text="Magnitude & Phase Angle.", font=('Helvetica',20)).grid(row=0, column=8)


    # ALL ABOUT COMPONENT1
    [chosen1_1, multiplier1_1] = Multiply()
    [chosen1_2, multiplier1_2] = Multiply()
    [Re1, Im1, Real1, Imag1] = Entry_Re_Im()
    label_Result1 = Entry(Frame, width=30, borderwidth=3, justify='center')
    [call_result1, buttonCalc1] = EnterButton(call_result, label_Result1, Re1, Im1, Real1, Imag1, chosen1_1, chosen1_2)

    # POSITIONS for Component1
    Real1.grid(row=2, column=1)
    multiplier1_1.grid(row=2, column=2, sticky=N+E+W+S)
    Imag1.grid(row=2, column=3)
    multiplier1_2.grid(row=2, column=4, sticky=N+E+W+S)
    Label(Frame, text="Component 1 = ").grid(row=2, column=0, sticky=E)
    label_Result1.place(x=275, y=460)

    # ALL ABOUT COMPONENT2
    [chosen2_1, multiplier2_1] = Multiply()
    [chosen2_2, multiplier2_2] = Multiply()
    [Re2, Im2, Real2, Imag2] = Entry_Re_Im()
    label_Result2 = Entry(Frame, width=30, borderwidth=3, justify='center')
    [call_result2, buttonCalc2] = EnterButton(call_result, label_Result2, Re2, Im2, Real2, Imag2, chosen2_1, chosen2_2)

    # POSITIONS for Component2
    Real2.grid(row=3, column=1)
    multiplier2_1.grid(row=3, column=2, sticky=N+E+W+S)
    Imag2.grid(row=3, column=3)
    multiplier2_2.grid(row=3, column=4, sticky=N+E+W+S)
    Label(Frame, text="Component 2 = ").grid(row=3, column=0, sticky=E)
    label_Result2.place(x=635, y=364)

    # ALL ABOUT COMPONENT3
    [chosen3_1, multiplier3_1] = Multiply()
    [chosen3_2, multiplier3_2] = Multiply()
    [Re3, Im3, Real3, Imag3] = Entry_Re_Im()
    label_Result3 = Entry(Frame, width=30, borderwidth=3, justify='center')
    [call_result3, buttonCalc3] = EnterButton(call_result, label_Result3, Re3, Im3, Real3, Imag3, chosen3_1, chosen3_2)

    # POSITIONS for Component3
    Real3.grid(row=4, column=1)
    multiplier3_1.grid(row=4, column=2, sticky=N+E+W+S)
    Imag3.grid(row=4, column=3)
    multiplier3_2.grid(row=4, column=4, sticky=N+E+W+S)
    Label(Frame, text="Component 3 = ").grid(row=4, column=0, sticky=E)
    label_Result3.place(x=968, y=460)

    # ALL ABOUT COMPONENT4
    [chosen4_1, multiplier4_1] = Multiply()
    [chosen4_2, multiplier4_2] = Multiply()
    [Re4, Im4, Real4, Imag4] = Entry_Re_Im()
    label_Result4 = Entry(Frame, width=30, borderwidth=3, justify='center')
    [call_result4, buttonCalc4] = EnterButton(call_result, label_Result4, Re4, Im4, Real4, Imag4, chosen4_1, chosen4_2)

    # POSITIONS for Component4
    Real4.grid(row=5, column=1)
    multiplier4_1.grid(row=5, column=2, sticky=N+E+W+S)
    Imag4.grid(row=5, column=3)
    multiplier4_2.grid(row=5, column=4, sticky=N+E+W+S)
    Label(Frame, text="Component 4 = ").grid(row=5, column=0, sticky=E)
    label_Result4.place(x=360, y=685)

    # ALL ABOUT COMPONENT5
    [chosen5_1, multiplier5_1] = Multiply()
    [chosen5_2, multiplier5_2] = Multiply()
    [Re5, Im5, Real5, Imag5] = Entry_Re_Im()
    label_Result5 = Entry(Frame, width=30, borderwidth=3, justify='center')
    [call_result5, buttonCalc5] = EnterButton(call_result, label_Result5, Re5, Im5, Real5, Imag5, chosen5_1, chosen5_2)

    # POSITIONS for Component5
    Real5.grid(row=6, column=1)
    multiplier5_1.grid(row=6, column=2, sticky=N+E+W+S)
    Imag5.grid(row=6, column=3)
    multiplier5_2.grid(row=6, column=4, sticky=N+E+W+S)
    Label(Frame, text="Component 5 = ").grid(row=6, column=0, sticky=E)
    label_Result5.place(x=965, y=700)


    # ALL about Vsource
    [chosen6_1, multiplier6_1] = Multiply()
    [Vsrc, VoltSour] = Entry_Source()
    label_Result6 = Entry(Frame, width=10, borderwidth=3, justify='center')
    [call_result6, buttonCalc6] = EnterButtonSource(call_resultVSource, label_Result6, Vsrc, VoltSour, chosen6_1)

    # POSITIONS for Vsource
    VoltSour.grid(row=7, column=1)
    multiplier6_1.grid(row=7, column=2, sticky=N+E+W+S)
    Label(Frame, text="Voltage Source = ").grid(row=7, column=0, sticky=E)
    label_Result6.place(x=205 , y=632)

    # ALL about Csource
    [chosen7_1, multiplier7_1] = Multiply()
    [Csrc, CurrSour] = Entry_Source()
    label_Result7 = Entry(Frame, width=10, borderwidth=3, justify='center')
    [call_result7, buttonCalc7] = EnterButtonSource(call_resultCSource, label_Result7, Csrc, CurrSour, chosen7_1)

    # POSITIONS for Csource
    CurrSour.grid(row=8, column=1)
    multiplier7_1.grid(row=8, column=2, sticky=N+E+W+S)
    Label(Frame, text="Current Source = ").grid(row=8, column=0, sticky=E)
    label_Result7.place(x=908, y=635)

    # OUTPUT
    # EVALUATE BUTTON
    EvalButton = Button(Frame, text='Evaluate', width=6, borderwidth=4, command=solve)
    EvalButton.config(bg='green3')
    EvalButton.grid(row=7, column=3, columnspan=1, sticky=N+E+W+S)

    # RESET BUTTON
    ResetButton = Button(Frame, text='Reset', width=6, borderwidth=4, command=reset)
    ResetButton.config(bg='red')
    ResetButton.grid(row=8, column=3, columnspan=1, sticky=N + E + W + S)

    # MESH I1
    Mesh_1 = Entry(Frame, width=19, borderwidth=3, justify='center')
    Mesh_1.place(x=310, y=615)
    Label(Frame, text="Mesh Current I1: ").grid(row=1, column=7, sticky=N + E + W + S)
    Angle1 = Entry(Frame, width=30, borderwidth=3, justify='center')
    Angle1.grid(row=1, column=8, columnspan=1, sticky=W)
    # MESH I2
    Mesh_2 = Entry(Frame, width=19, borderwidth=3, justify='center')
    Mesh_2.place(x=668, y=615)
    Label(Frame, text="Mesh Current I2: ").grid(row=2, column=7, sticky=N + E + W + S)
    Angle2 = Entry(Frame, width=30, borderwidth=3, justify='center')
    Angle2.grid(row=2, column=8, columnspan=1, sticky=W)
    # MESH I3
    Mesh_3 = Entry(Frame, width=19, borderwidth=3, justify='center')
    Mesh_3.place(x=1017, y=615)
    Label(Frame, text="Mesh Current I3: ").grid(row=3, column=7, sticky=N + E + W + S)
    Angle3 = Entry(Frame, width=30, borderwidth=3, justify='center')
    Angle3.grid(row=3, column=8, columnspan=1, sticky=W)
    # MESH I4
    Mesh_4 = Entry(Frame, width=30, borderwidth=3, justify='center')
    Mesh_4.place(x=635, y=445)
    Label(Frame, text="Mesh Current I4: ").grid(row=4, column=7, sticky=N + E + W + S)
    Angle4 = Entry(Frame, width=30, borderwidth=3, justify='center')
    Angle4.grid(row=4, column=8, columnspan=1, sticky=W)


    Frame.mainloop()
    return
