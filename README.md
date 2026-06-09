# Driver Validation Framework

A modular embedded driver validation and hardware interface testing framework built in Python using PyTest and PySerial for validating GPIO, UART, SPI, I2C, and DMA driver behavior. The framework supports peripheral initialization validation, input/output verification, interrupt validation, communication protocol testing, transfer integrity verification, bus recovery validation, fault injection, automated regression testing, validation report generation, structured logging, and reusable driver validation components for embedded systems and hardware quality assurance workflows.

---

## Features

### GPIO Driver Validation

- GPIO initialization validation
- GPIO configuration validation
- Input operation validation
- Output operation validation
- Pull-up validation
- Pull-down validation
- Interrupt validation
- Fault injection testing

### UART Driver Validation

- Baud rate validation
- Transmission validation
- Reception validation
- Buffer overflow validation
- Timeout validation
- Framing error validation

### SPI Driver Validation

- Master mode validation
- Slave mode validation
- CPOL validation
- CPHA validation
- Transfer integrity validation
- Multi-device validation

### I2C Driver Validation

- Device addressing validation
- Read operation validation
- Write operation validation
- NACK handling validation
- Bus mismatch detection
- Bus recovery validation

### DMA Driver Validation

- DMA configuration validation
- Transfer start validation
- Transfer completion validation
- Interrupt generation validation
- Error handling validation

### Fault Injection

- Invalid configuration testing
- Communication fault simulation
- Invalid state testing
- Peripheral fault testing
- Driver recovery testing

### Reporting

- Automated validation reports
- Driver validation summaries
- Regression execution reports

### Automation

- Automated regression runners
- PyTest-based validation suites
- Reusable driver tester modules

---

## Project Structure

```text
driver_validation/

├── automation/
│   ├── regression_runner.py
│   ├── gpio_regression_runner.py
│   ├── uart_regression_runner.py
│   ├── spi_regression_runner.py
│   ├── i2c_regression_runner.py
│   ├── dma_regression_runner.py
│   ├── gpio_report_generator.py
│   ├── uart_report_generator.py
│   ├── spi_report_generator.py
│   ├── i2c_report_generator.py
│   └── dma_report_generator.py
│
├── fault_injection/
│   └── gpio_fault_injector.py
│
├── reports/
│   ├── gpio_test_plan.md
│   ├── uart_test_plan.md
│   ├── spi_test_plan.md
│   ├── i2c_test_plan.md
│   └── dma_test_plan.md
│
├── test_runner/
│   ├── device_interface.py
│   ├── fake_serial.py
│   └── serial_client.py
│
├── tests/
│   ├── gpio_driver_tests/
│   ├── uart_driver_tests/
│   ├── spi_driver_tests/
│   ├── i2c_driver_tests/
│   └── dma_driver_tests/
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```



## Technologies

- Python
- PyTest
- PySerial


## Running the Project

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### Run All Tests

```bash
python3 -m pytest
```

### Run GPIO Tests

```bash
pytest -m gpio
```

### Run UART Tests

```bash
pytest -m uart
```

### Run SPI Tests

```bash
pytest -m spi
```

### Run I2C Tests

```bash
pytest -m i2c
```

### Run DMA Tests

```bash
pytest -m dma
```




## Future Extensions

- Real STM32 hardware integration
- Hardware-in-the-loop testing
- Logic analyzer integration
- Oscilloscope-based timing validation
- CAN driver validation
- USB driver validation
- Ethernet driver validation
- HTML report generation
- JSON report export
- CI/CD validation pipeline
- Performance benchmarking
- Coverage reporting