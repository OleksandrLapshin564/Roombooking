import os

template_dir = "./booking/templates/booking"
output_file = "template_report.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in sorted(os.listdir(template_dir)):
        if filename.endswith(".html"):
            filepath = os.path.join(template_dir, filename)
            size = os.path.getsize(filepath)
            f.write(f"{filename} — {size} bytes\n")

print(f"Report saved to {output_file}")
