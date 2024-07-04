import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QDoubleSpinBox,
    QSpinBox,
    QDateEdit,
    QTextEdit,
    QFileDialog,
    QLabel,
    QScrollArea,
    QAction,
    QMainWindow,
)
from PyQt5.QtGui import QPalette, QColor, QPixmap, QLinearGradient, QBrush, QIcon
from PyQt5.QtCore import Qt
from fpdf import FPDF

class EstimateGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estimate Generator")

        self.setWindowIcon(QIcon('D:\\Vscodes\\my estimate generator app\\Squid Boss.png'))  # Replace with your icon path

        # Create a gradient that fades from sky blue to black
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(135, 206, 235))  # Sky blue
        

        # Create a palette and set the gradient as the background
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # black text

        self.setPalette(palette)
        self.setAutoFillBackground(True)
    
       # Main Layout
        self.main_layout = QVBoxLayout()      
        

        # Logo Area
        logo_frame = QFrame(self)
        logo_layout = QHBoxLayout()  # Use QHBoxLayout for logo area
        logo_frame.setLayout(logo_layout)

        self.logo_label = QLabel()
        self.logo_label.setFixedSize(200, 100)  # Set a fixed size for the logo
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setStyleSheet("border: 1px;")
        
         # Customer Information
        customer_frame = QFrame(self)
        customer_layout = QVBoxLayout()  # Use QVBoxLayout for columns
        customer_frame.setLayout(customer_layout)

        name_label = QLabel("Company Name:")
        self.name_entry = QLineEdit()
        self.name_entry.setFixedWidth(300)  # Set fixed width for name entry
        self.name_entry.setStyleSheet("border-radius: 5px;")
        customer_layout.addWidget(name_label)
        customer_layout.addWidget(self.name_entry)

        phone_label = QLabel("Company Phone:")
        self.phone_entry = QLineEdit()
        self.phone_entry.setFixedWidth(300)  # Set fixed width for phone entry
        self.phone_entry.setStyleSheet("border-radius: 5px;")
        customer_layout.addWidget(phone_label)
        customer_layout.addWidget(self.phone_entry)

        name_label = QLabel("Customer Name:")
        self.name_entry = QLineEdit()
        self.name_entry.setFixedWidth(300)  # Set fixed width for name entry
        self.name_entry.setStyleSheet("border-radius: 5px;")
        customer_layout.addWidget(name_label)
        customer_layout.addWidget(self.name_entry)

        phone_label = QLabel("Phone:")
        self.phone_entry = QLineEdit()
        self.phone_entry.setFixedWidth(300)  # Set fixed width for phone entry
        self.phone_entry.setStyleSheet("border-radius: 5px;")
        customer_layout.addWidget(phone_label)
        customer_layout.addWidget(self.phone_entry)

        address_label = QLabel("Address:")
        self.address_entry = QLineEdit()
        self.address_entry.setFixedWidth(300)  # Set fixed width for address entry
        self.address_entry.setStyleSheet("border-radius: 5px;")
        customer_layout.addWidget(address_label)
        customer_layout.addWidget(self.address_entry)

        # Project Details
        project_frame = QFrame(self)
        project_layout = QVBoxLayout()  # Use QVBoxLayout for columns
        project_frame.setLayout(project_layout)

        project_name_label = QLabel("Project Name:")
        self.project_name_entry = QLineEdit()
        self.project_name_entry.setFixedWidth(200)  # Set fixed width for project name entry
        self.project_name_entry.setStyleSheet("border-radius: 5px;")
        project_layout.addWidget(project_name_label)
        project_layout.addWidget(self.project_name_entry)

        # Add Date Input
        date_label = QLabel("Date:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setFixedWidth(200)
        self.date_edit.setStyleSheet("border-radius: 5px;")
        project_layout.addWidget(date_label)
        project_layout.addWidget(self.date_edit)

    
        # Add widgets to main layout
        self.main_layout.addWidget(customer_frame)  # Customer info on the left
        self.main_layout.addWidget(project_frame)  # Project details on the right

        # Notes Area
        notes_frame = QFrame(self)
        notes_layout = QVBoxLayout()
        notes_frame.setLayout(notes_layout)

        notes_label = QLabel("Notes:")
        notes_layout.addWidget(notes_label)

        self.notes_edit = QTextEdit()
        notes_layout.addWidget(self.notes_edit)
        self.main_layout.addWidget(notes_frame)  # Add notes frame

        # Project Items
        item_frame = QFrame(self)
        self.item_layout = QGridLayout()  # Define item_layout here
        item_frame.setLayout(self.item_layout)

        self.num_items = 1
        self.add_item_button = QPushButton("Add Item")
        self.add_item_button.clicked.connect(self.add_item)
        self.item_layout.addWidget(self.add_item_button, 0, 0, Qt.AlignCenter)
        self.add_item_button.setFixedWidth(200)
        self.add_item_button.setStyleSheet("background-color: blue; color: white;")
        
        self.create_item_row(1)

                # Delete Item Button
        self.delete_item_button = QPushButton("Delete Item")
        self.delete_item_button.clicked.connect(self.delete_item)
        self.item_layout.addWidget(self.delete_item_button, 0, 1, Qt.AlignRight)
        self.delete_item_button.setFixedWidth(200)
        self.delete_item_button.setStyleSheet("background-color: grey; color: white;")


       # Create a scroll area to contain the item layout
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Allow the scroll area to resize
        self.scroll_area.setWidget(item_frame)  # Set the item layout as the widget

        self.main_layout.addWidget(self.scroll_area)  # Add scroll area to the main layout


              
        

        # Tax Input
        self.tax_label = QLabel("Tax Rate (%):")
        self.tax_entry = QDoubleSpinBox()
        self.tax_entry.setRange(0, 100)
        self.tax_entry.setSingleStep(0.1)
        self.tax_entry.setFixedWidth(200)
        self.tax_entry.setStyleSheet("border-radius: 5px;")
        self.item_layout.addWidget(self.tax_label, 2, 2)
        self.item_layout.addWidget(self.tax_entry, 2, 3)
        self.item_layout.setSpacing(10)  # Set spacing between widgets

        # Calculate Button
        calculate_button = QPushButton("Calculate Estimate")
        calculate_button.clicked.connect(self.calculate_estimate)
        calculate_button.setStyleSheet("background-color: green; color: black;")
        calculate_button.setFixedWidth(500)
        self.main_layout.addWidget(calculate_button,alignment=Qt.AlignCenter)
        

        # Set margins to 0 for all layouts
        customer_layout.setContentsMargins(0, 0, 0, 0)
        project_layout.setContentsMargins(0, 0, 0, 0)
        self.item_layout.setContentsMargins(0, 0, 0, 0)

        # Initialize logo path
        self.logo_path = None

        # Logo Area
        logo_frame = QFrame(self)
        logo_layout = QHBoxLayout()  # Use QHBoxLayout for logo area
        logo_frame.setLayout(logo_layout)

        self.logo_label = QLabel()
        self.logo_label.setFixedSize(200, 100)  # Set a fixed size for the logo
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setStyleSheet("border: 1px;")

        self.upload_button = QPushButton("Upload Logo")
        self.upload_button.clicked.connect(self.upload_logo)

        # Add the upload button to the top right corner
        logo_layout.addWidget(self.logo_label, alignment=Qt.AlignLeft)
        logo_layout.addWidget(self.upload_button, alignment=Qt.AlignRight)

        # Add the logo frame to the top of the main layout
        self.main_layout.insertWidget(0, logo_frame)  # Insert at index 0

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def create_item_row(self, row_num):
        item_label = QLabel(f"Item {row_num}:")
        item_entry = QLineEdit()
        item_entry.setFixedWidth(500)  # Set fixed width for item entry
        item_entry.setStyleSheet("border-radius: 5px;")

        # Create a layout for the item label and entry
        item_layout = QVBoxLayout()  # Use QVBoxLayout to stack vertically
        item_layout.addWidget(item_label)  # Add label on top
        item_layout.addWidget(item_entry)  # Add entry below
        
        # Add Quantity Label and Entry
        quantity_label = QLabel("Quantity:")
        quantity_entry = QSpinBox()
        quantity_entry.setRange(1, 100)  # Set range for quantity
        quantity_entry.setFixedWidth(100)  # Set fixed width for quantity entry
        quantity_entry.setStyleSheet("border-radius: 5px;")

        # Create a layout for the quantity label and entry
        quantity_layout = QVBoxLayout()
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(quantity_entry)


        price_label = QLabel("Price:")
        price_entry = QDoubleSpinBox()
        price_entry.setRange(0, 10000)
        price_entry.setSingleStep(0.5)
        price_entry.setFixedWidth(200)  # Set fixed width for price entry
        price_entry.setStyleSheet("border-radius: 5px;")

        # Create a layout for the price label and entry
        price_layout = QVBoxLayout()
        price_layout.addWidget(price_label)
        price_layout.addWidget(price_entry)

        
        # Add Total Price Label and Entry
        total_price_label = QLabel("Total Price:")
        total_price_entry = QLabel("")  # Use QLabel for total price display
        total_price_entry.setFixedWidth(200)  # Set fixed width for total price entry
        total_price_entry.setStyleSheet("border-radius: 5px;")

        # Create a layout for the total price label and entry
        total_price_layout = QVBoxLayout()
        total_price_layout.addWidget(total_price_label)
        total_price_layout.addWidget(total_price_entry)

        # Use the existing layout
        self.item_layout.addWidget(item_label, row_num, 0)
        self.item_layout.addWidget(item_entry, row_num, 1)
        self.item_layout.addWidget(quantity_label, row_num, 2)
        self.item_layout.addWidget(quantity_entry, row_num, 3)
        self.item_layout.addWidget(price_label, row_num, 4)
        self.item_layout.addWidget(price_entry, row_num, 5)
        self.item_layout.addWidget(total_price_label, row_num, 6)
        self.item_layout.addWidget(total_price_entry, row_num, 7)  # Add total price layout
        self.item_layout.setSpacing(10)  # Set spacing to 0 for item_layout

        setattr(self, f"item{row_num}_entry", item_entry)
        setattr(self, f"quantity{row_num}_entry", quantity_entry)
        setattr(self, f"price{row_num}_entry", price_entry)
        setattr(self, f"total_price{row_num}_entry", total_price_entry)  # Store total price entry


    def add_item(self):
        self.num_items += 1
        self.create_item_row(self.num_items)
        self.item_layout.addWidget(self.tax_entry, self.num_items + 1, 3)
        self.item_layout.addWidget(self.tax_label, self.num_items + 1, 2)
        self.total_prices() 
    
    def delete_item(self):
        if self.num_items > 1:
            # Delete the last row of items
            for column in range(8):
                item = self.item_layout.itemAtPosition(self.num_items - 1, column)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        self.item_layout.removeWidget(widget)
                        widget.deleteLater()

            # Remove the attributes associated with the deleted row
            delattr(self, f"item{self.num_items - 1}_entry")
            delattr(self, f"quantity{self.num_items - 1}_entry")
            delattr(self, f"price{self.num_items - 1}_entry")
            delattr(self, f"total_price{self.num_items - 1}_entry")

            self.num_items -= 1

            # Call total_prices AFTER deleting attributes
        self.total_prices()

            # Reposition the tax label and entry (if they were removed)
        if self.num_items > 1:
                self.item_layout.addWidget(self.tax_label, self.num_items + 1, 2)
                self.item_layout.addWidget(self.tax_entry, self.num_items + 1, 3)



    def total_prices(self):
        # Start the loop from 1 to avoid accessing 'quantity1_entry' before it's created
        for i in range(1, self.num_items + 1):
            quantity = getattr(self, f"quantity{i}_entry").value()
            price = getattr(self, f"price{i}_entry").value()
            total_price = quantity * price
            total_price_entry = getattr(self, f"total_price{i}_entry")
            total_price_entry.setText(f"${total_price:.2f}")       
    
    def calculate_estimate(self):
        company_name = self.name_entry.text()
        company_phone = self.phone_entry.text()
        customer_name = self.name_entry.text()
        customer_phone = self.phone_entry.text()
        customer_address = self.address_entry.text()
        project_name = self.project_name_entry.text()
        tax_rate = self.tax_entry.value() / 100
        project_date = self.date_edit.date().toString("yyyy-MM-dd")  # Get date as string
        notes = self.notes_edit.toPlainText()  # Get notes from QTextEdit

        item_prices = []
        for i in range(1, self.num_items + 1):
            quantity = getattr(self, f"quantity{i}_entry").value()  # Get quantity
            price = getattr(self, f"price{i}_entry").value()
            item_prices.append(quantity * price)  # Calculate price based on quantity

        total_cost = sum(item_prices) 
        total_cost *= (1 + tax_rate)

        class PDF(FPDF):
         def header(self):
          self.set_font("Arial", "B", 12)
          self.cell(0, 10, "Estimate", 0, 1, "C")
          self.ln(10)

        def footer(self):
          self.set_y(-15)
          self.set_font("Arial", "I", 8)
          self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        pdf = PDF()
        pdf.add_page()

  
# Project Details
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Project: {project_name}", 0, 1, "R")
        pdf.cell(0, 10, f"Date: {project_date}", 0, 1, "R")
        pdf.ln(10)  # Add a line break

# company information
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Company Information", 0, 1)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Name: {company_name}", 0, 1)
        pdf.cell(0, 10, f"Phone: {company_phone}", 0, 1)
        pdf.ln(10)  # Add a line break


# Customer Information with Box
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, "Customer Information", 0, 1)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, f"Name: {customer_name}", 0, 1, fill=True)
        pdf.cell(0, 10, f"Phone: {customer_phone}", 0, 1, fill=True)
        pdf.cell(0, 10, f"Address: {customer_address}", 0, 1, fill=True)
        pdf.ln(10)  # Add a line break

# Items Table
        pdf.cell(0, 10, "Items", 0, 1)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(10, 10, "#", 1)
        pdf.cell(100, 10, "Description", 1)
        pdf.cell(30, 10, "Quantity", 1)
        pdf.cell(40, 10, "Price", 1)
        pdf.cell(40, 10, "Total Price", 1)  # Add Total Price column
        pdf.ln()
        pdf.set_font("Arial", "", 12)
        for i, price in enumerate(item_prices):
            quantity = getattr(self, f"quantity{i + 1}_entry").value()
            total_price = quantity * price
            pdf.cell(10, 10, str(i+1), 1)
            pdf.cell(100, 10, f"Item {i+1}", 1)
            pdf.cell(30, 10, str(quantity), 1)
            pdf.cell(40, 10, f"${price:.2f}", 1)
            pdf.cell(40, 10, f"${total_price:.2f}", 1)  # Add total price to table
            pdf.ln()
            pdf.ln(10)
  # Add a line break

# Tax
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Tax and Total", 0, 1)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, f"Tax Rate: {tax_rate * 100:.1f}%", 0, 1)
        pdf.cell(0, 10, f"Total Cost: ${total_cost:.2f}", 0, 1)
        pdf.ln(10)  # Add a line break

# Notes Section with Box
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Notes", 0, 1)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, notes, border=1)
        pdf.ln(10)  # Add a line break

        # Signature Section
        pdf.set_font("Arial", "B", 12)
        pdf.cell(30, 10, "Signature:", 0, 0)  # Label for customer signature with reduced width
        pdf.set_font("Arial", "", 12)
        pdf.cell(70, 10, "_________________________", 0, 0)  # Line for customer signature with increased width

        pdf.set_font("Arial", "B", 12)
        pdf.cell(15, 10, "Date:", 0, 0)  # Label for date
        pdf.set_font("Arial", "", 12)
        pdf.cell(50, 10, "_________________________", 0, 1)  # Line for date

        pdf.ln(5)
  

         # Add logo to PDF if available
        if self.logo_path:
            pdf.image(self.logo_path, x=10, y=10, w=50, h=20)  # Adjust position and size as needed


        # Save PDF
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Estimate", "estimate.pdf", "PDF Files (*.pdf)"
        )
        if file_path:
          pdf.output(file_path)
 
    def upload_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Logo", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_path:
            self.set_logo(file_path)

    def set_logo(self, file_path):
        pixmap = QPixmap(file_path)
        self.logo_label.setPixmap(pixmap.scaled(self.logo_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EstimateGenerator()
    window.show()
    sys.exit(app.exec_())
