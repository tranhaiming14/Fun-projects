import subprocess
class Reservation:
    def __init__(self, guest, paid, room):
        self.guest = guest
        self.paid = paid
        self.room = room
    def __str__(self):
        return f"Guest: {self.guest}, Paid: {self.paid}, Room: {self.room}"
class LongReservation(Reservation):
    def __init__(self, guest, paid, room, month):
        super().__init__(guest, paid, room)
        self.month = month
    def greet(self):
        return f"Hello you are staying for{self.month}"
    def save(self, filename):
        try:
            with open(filename, "w") as f:
                f.write(f"Guest: {self.guest}\n")
                f.write(f"Paid: {self.paid}\n")
                f.write(f"Room: {self.room}\n")
                f.write(f"Months: {self.month}\n")
            print(f"Reservation details saved to {filename}.")
        except Exception as e:
            print(f"Error saving reservation details: {e}")
    def save_compress(self, filename):
        try:
            self.save(filename)
            subprocess.run(['7z', 'a', f"{filename}.zip", filename])              
            print(f"Reservation details compressed into {filename}.zip.")
        except Exception as e:
            print(f"Error during compression: {e}")

Lam_Reservation = LongReservation("Lam", True, 1, 3)
print(Lam_Reservation)
Lam_Reservation.save("res")
Lam_Reservation.save_compress("res")
        