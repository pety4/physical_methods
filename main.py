import tkinter as tk

# Экспертная оценка
expScores = [0] * 4
# Личная оценка
selfScores = [0] * 4
# Критерии оценивания
criterion = ["Тест", "Круг общения", "Самореализация", "Влияние среды", "Тест", "Тест1", "Тест 3"]


def result():
    global selfScores
    global expScores
    window.destroy()
    resWindow = tk.Tk()
    resWindow.title("Результат")
    frm_form = tk.Frame(master=resWindow,
                        relief=tk.SUNKEN,
                        borderwidth=3,
                        width=200,
                        height=100)
    frm_form.pack(fill=tk.BOTH,
                  side=tk.LEFT,
                  expand=True)
    lbl_result = tk.Label(master=frm_form,
                          text="Результат:",
                          font=("Times New Roman", 18))
    lbl_result.grid(row=0,
                    column=0)
    rowCount = 1
    for i in range(len(expScores)):
        if (expScores[i] < 3) or (selfScores[i] < 3):
            lbl_lowScore = tk.Label(master=frm_form,
                                    text="Один из параметров критически мал, обратитесь к специалисту",
                                    font=("Times New Roman", 18))
            lbl_lowScore.grid(row=rowCount,
                              column=0)
            rowCount += 1
            break
        if abs(expScores[i] - selfScores[i]) >= 2:
            lbl_lowScore = tk.Label(master=frm_form,
                                    text="Экспертная оценка отличается от Вашей на недопустимую величину, обратитесь к специалисту",
                                    font=("Times New Roman", 18))
            lbl_lowScore.grid(row=rowCount,
                              column=0)
            rowCount += 1
            break
    if rowCount == 1:
        lbl_lowScore = tk.Label(master=frm_form,
                                text="С Вами всё хорошо",
                                font=("Times New Roman", 18))
    lbl_lowScore.grid(row=rowCount,
                      column=0)
    resWindow.mainloop()


def exp():
    def expAccept():
        global expScores
        for i in range(len(criterion)):
            expScores[i] = entry[i].get()
        expWindow.destroy()
    from tkinter.messagebox import askyesno
    result = askyesno(title="Подтверждение квалификации",
                      message="Данная форма заполняется экспертом\n"
                              "Вы точно эксперт?")
    if result == False:
        return
    expWindow = tk.Tk()
    rowCount = 0
    expWindow.title("Экспертная оценка")
    frm_form = tk.Frame(master=expWindow,
                        relief=tk.SUNKEN,
                        borderwidth=3,
                        width=200,
                        height=100)
    frm_form.pack(fill=tk.BOTH,
                  side=tk.LEFT,
                  expand=True)
    instruction = tk.Label(master=frm_form,
                           text="Оцените состояние пациента\n"
                                "5-отлично\n"
                                "4-хорошо\n"
                                "3-удовлетворительно\n"
                                "2-неудовлетворительно\n"
                                "1-ужасно",
                           font=("Times New Roman", 18))
    instruction.grid(row=0,
                     column=0,
                     columnspan=2)
    rowCount+=1
    entry = [tk.Entry(master=frm_form, width=20, font=("Times New Roman", 18)) for i in range(len(criterion))]
    for i in range(len(criterion)):
        entry[i].grid(row=i + rowCount, column=1)
    for i, text in enumerate(criterion, start=rowCount):
        label = tk.Label(master=frm_form, text=text + ":", font=("Times New Roman", 18))
        label.grid(row=i, column=0, sticky="e")
    rowCount+=len(criterion)
    # Кнопки
    btn_accept = tk.Button(master=frm_form,
                           text="Принять",
                           font=("Times New Roman", 18),
                           command=expAccept)
    btn_accept.grid(row=rowCount,
                    column=0,
                    columnspan=2)
    rowCount+=1
    expWindow.mainloop()


def accept():
    global selfScores
    for i in range(len(criterion)):
        score[i]["text"] = f"{expScores[i]}"
    for i in range(len(criterion)):
        selfScores[i]=entry[i].get()


window = tk.Tk()
rowCount=0;
window.title("Анализ личности")
frm_form = tk.Frame(master=window,
                    relief=tk.SUNKEN,
                    borderwidth=3,
                    width=200,
                    height=100)
frm_form.pack(fill=tk.BOTH,
              side=tk.LEFT,
              expand=True)
instruction = tk.Label(master=frm_form,
                       text="Оцените своё состояние\n"
                            "5-отлично\n"
                            "4-хорошо\n"
                            "3-удовлетворительно\n"
                            "2-неудовлетворительно\n"
                            "1-ужасно",
                       font=("Times New Roman", 18))
instruction.grid(row=rowCount,
                 column=0,
                 columnspan=2)
rowCount+=1
entry=[tk.Entry(master=frm_form, width=20, font=("Times New Roman", 18)) for i in range(len(criterion))]
for i in range(len(criterion)):
    entry[i].grid(row=i+rowCount, column=1)
for i, text in enumerate(criterion, start=rowCount):
    label = tk.Label(master=frm_form, text=text+":", font=("Times New Roman", 18))
    label.grid(row=i, column=0, sticky="e")
rowCount+=len(criterion)
# Кнопки
btn_accept = tk.Button(master=frm_form,
                       text="Принять",
                       font=("Times New Roman", 18),
                       command=accept)
btn_accept.grid(row=rowCount,
                column=0,
                columnspan=2)
rowCount+=1
btn_result = tk.Button(master=frm_form,
                       text="Получить результат",
                       font=("Times New Roman", 18),
                       command=result)
btn_result.grid(row=rowCount,
                column=0,
                columnspan=2)
# Экспертная оценка
rowCount=0
lbl_text = tk.Label(master=frm_form,
                    text="Экспертная оценка Вашего состояния",
                    font=("Times New Roman", 18))
lbl_text.grid(row=rowCount,
              column=3,
              columnspan=2)
rowCount+=1
score=[tk.Label(master=frm_form, text="", font=("Times New Roman", 18)) for i in range(len(criterion))]
for i, text in enumerate(criterion, start=rowCount):
    label = tk.Label(master=frm_form, text=text + ":", font=("Times New Roman", 18))
    label.grid(row=i, column=3, sticky="e")
    score[i-1].grid(row=i, column=4, sticky="w")
rowCount+=len(criterion)
btn_exp = tk.Button(master=frm_form,
                    text="Ввести экспертную оценку",
                    font=("Times New Roman", 18),
                    command=exp)
btn_exp.grid(row=rowCount,
             column=3,
             columnspan=2)
window.mainloop()
