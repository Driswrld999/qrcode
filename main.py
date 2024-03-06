from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from pyzbar import pyzbar


class QRCodeScanner(BoxLayout):
    def on_qr_decoded(self, instance, barcodes):
        for barcode in barcodes:
            barcode_data = barcode.data.decode("utf-8")
            self.ids.qr_label.text = f"QR Code Data: {barcode_data}"


class QRCodeScannerApp(App):
    def build(self):
        return QRCodeScanner()


if __name__ == '__main__':
    QRCodeScannerApp().run()