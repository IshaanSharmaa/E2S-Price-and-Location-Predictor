from E2S_GUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
import joblib

df = pd.read_excel("final_dataset_x2s.xlsx")

test_dict = {
    'Seller State': 'New Delhi',
    'Seller Location': 'New Delhi - North West Delhi',
    'Product Group': 'Telecom & Mobility',
    'Product Category': 'Mobile Phones',
    'Product Subcategory': 'Smart Phones',
    'Product Offered': 'Apple iPhone 13 (128GB)',
    'Qty': 100,
    'Actual Price': 57882,
    'Seller Price': 57669.49
}

test_df = pd.DataFrame([test_dict])

price_predictor = joblib.load('e2s_price_prediction.joblib')
location_predictor = joblib.load('e2s_location_prediction.joblib')
encoder = joblib.load('e2s_data_encoder1.joblib')


class code(object):
    def __init__(self, object):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(object)
        object.show()
        pass

    def reset_data(self):
        self.ui.comboBox_state.clear(),
        self.ui.comboBox_location.clear(),
        self.ui.comboBox_group.clear(),
        self.ui.comboBox_category.clear(),
        self.ui.comboBox_subcategory.clear(),
        self.ui.comboBox_offered.clear(),
        self.ui.doubleSpinBox_quantity.clear(),
        self.ui.doubleSpinBox_actual_price.clear(),
        self.ui.doubleSpinBox_seller_price.clear()
        self.ui.lcdNumber.display(0)
        self.ui.label_p_location.setText("")

        self.ui.pushButton.clicked.connect(self.set_data)

    def set_data(self):

        self.ui.comboBox_state.addItems(
            sorted(list(df["Seller State"].unique())))

        self.ui.comboBox_state.activated.connect(
            lambda: self.ui.comboBox_location.addItems(
                sorted(
                    list(df.loc[df["Seller State"] == self.ui.comboBox_state.
                                currentText(), "Seller Location"].unique()))))

        self.ui.comboBox_group.addItems(
            sorted(list(df["Product Group"].unique())))

        self.ui.comboBox_group.activated.connect(
            lambda: self.ui.comboBox_category.addItems(
                sorted(
                    list(df.loc[df["Product Group"] == self.ui.comboBox_group.
                                currentText(), "Product Category"].unique()))))

        self.ui.comboBox_category.activated.connect(
            lambda: self.ui.comboBox_subcategory.addItems(
                sorted(
                    list(df.loc[df["Product Category"
                                   ] == self.ui.comboBox_category.currentText(
                                   ), "Product Subcategory"].unique()))))

        self.ui.comboBox_subcategory.activated.connect(
            lambda: self.ui.comboBox_offered.addItems(
                sorted(
                    list(df.loc[df["Product Subcategory"] == self.ui.
                                comboBox_subcategory.currentText(
                                ), "Product Offered"].unique()))))

        self.ui.pushButton_2.clicked.connect(self.predict)
        self.ui.pushButton_3.clicked.connect(self.reset_data)

    # def read_data(self):

    #     read_df = pd.DataFrame([[
    #         self.ui.comboBox_state.currentText(),
    #         self.ui.comboBox_location.currentText(),
    #         self.ui.comboBox_group.currentText(),
    #         self.ui.comboBox_category.currentText(),
    #         self.ui.comboBox_subcategory.currentText(),
    #         self.ui.comboBox_offered.currentText(),
    #         self.ui.doubleSpinBox_quantity.value(),
    #         self.ui.doubleSpinBox_actual_price.value(),
    #         self.ui.doubleSpinBox_seller_price.value()
    #     ]],
    #                            columns=test_dict.keys())

    #     self.ui.pushButton_2.clicked.connect(self.predict(read_df))
    #     pass

    def predict(self):

        read_df = pd.DataFrame([[
            self.ui.comboBox_state.currentText(),
            self.ui.comboBox_location.currentText(),
            self.ui.comboBox_group.currentText(),
            self.ui.comboBox_category.currentText(),
            self.ui.comboBox_subcategory.currentText(),
            self.ui.comboBox_offered.currentText(),
            self.ui.doubleSpinBox_quantity.value(),
            self.ui.doubleSpinBox_actual_price.value(),
            self.ui.doubleSpinBox_seller_price.value()
        ]],
                               columns=test_dict.keys())

        # transformed_x_np = encoder.transform(read_df)

        transformed_x = pd.DataFrame(encoder.transform(read_df),
                                     columns=[
                                         'Seller State', 'Seller Location',
                                         'Product Group', 'Product Category',
                                         'Product Subcategory',
                                         'Product Offered', 'Qty',
                                         'Actual Price', 'Seller Price'
                                     ])

        transformed_x_price = transformed_x.drop(
            ["Seller State", "Seller Location"], axis=1)
        transformed_x_location = transformed_x.drop(
            ['Qty', 'Actual Price', 'Seller Price'], axis=1)

        self.ui.lcdNumber.display('{:.02f}'.format(
            price_predictor.predict(transformed_x_price)[0]))
        print(price_predictor.predict(transformed_x_price)[0])
        self.ui.label_p_location.setText(
            location_predictor.predict(transformed_x_location)[0])
        self.ui.label_p_location.adjustSize()

        read_df.drop(read_df.index)
        transformed_x.drop(transformed_x.index)
        transformed_x_price.drop(transformed_x_price.index)
        transformed_x_location.drop(transformed_x_location.index)
        # np.delete(transformed_x_np)

        self.ui.pushButton_3.clicked.connect(self.reset_data)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = code(MainWindow)
    ui.reset_data()
    sys.exit(app.exec_())