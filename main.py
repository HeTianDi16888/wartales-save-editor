import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import shutil
from datetime import datetime


class WartalesEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Wartales Save Editor")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        self.data = None
        self.filepath = None
        self.current_character = None
        self.characters = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main UI"""
        # Top frame for file operations
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        ttk.Button(top_frame, text="Open Save File", command=self.open_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Save Changes", command=self.save_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Create Backup", command=self.create_backup).pack(side=tk.LEFT, padx=5)
        
        self.file_label = ttk.Label(top_frame, text="No file loaded", relief=tk.SUNKEN)
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        
        # Main content frame
        content_frame = ttk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Character list
        left_frame = ttk.LabelFrame(content_frame, text="Characters & Companions", width=250)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Listbox for characters
        self.char_listbox = tk.Listbox(left_frame, height=20)
        self.char_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.char_listbox.bind('<<ListboxSelect>>', self.on_character_select)
        
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.char_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.char_listbox.config(yscrollcommand=scrollbar.set)
        
        # Right panel - Character details
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Notebook with tabs
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Stats tab
        self.stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_frame, text="Stats")
        self.setup_stats_tab()
        
        # Traits tab
        self.traits_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.traits_frame, text="Traits")
        self.setup_traits_tab()
        
        # Equipment tab
        self.equipment_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.equipment_frame, text="Equipment")
        self.setup_equipment_tab()
        
        # Inventory tab
        self.inventory_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_frame, text="Inventory")
        self.setup_inventory_tab()
    
    def setup_stats_tab(self):
        """Setup stats editing tab"""
        canvas = tk.Canvas(self.stats_frame)
        scrollbar = ttk.Scrollbar(self.stats_frame, orient=tk.VERTICAL, command=canvas.scroll)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.stats_entries = {}
        
        # Basic Stats
        ttk.Label(scrollable_frame, text="Basic Stats", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=10, pady=10)
        
        basic_stats = ["level", "health", "maxHealth", "experience"]
        row = 1
        for stat in basic_stats:
            ttk.Label(scrollable_frame, text=stat).grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(scrollable_frame, width=15)
            entry.grid(row=row, column=1, sticky=tk.W, padx=10, pady=5)
            self.stats_entries[stat] = entry
            row += 1
        
        # Core Stats
        ttk.Label(scrollable_frame, text="Core Stats", font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, sticky=tk.W, padx=10, pady=(20, 10))
        row += 1
        
        core_stats = ["strength", "constitution", "dexterity", "speed", "intelligence", "wisdom"]
        for stat in core_stats:
            ttk.Label(scrollable_frame, text=stat).grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(scrollable_frame, width=15)
            entry.grid(row=row, column=1, sticky=tk.W, padx=10, pady=5)
            self.stats_entries[stat] = entry
            row += 1
        
        # Additional stats
        ttk.Label(scrollable_frame, text="Additional Stats", font=("Arial", 12, "bold")).grid(row=row, column=0, columnspan=2, sticky=tk.W, padx=10, pady=(20, 10))
        row += 1
        
        additional_stats = ["armor", "dodge", "critChance", "initiative"]
        for stat in additional_stats:
            ttk.Label(scrollable_frame, text=stat).grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(scrollable_frame, width=15)
            entry.grid(row=row, column=1, sticky=tk.W, padx=10, pady=5)
            self.stats_entries[stat] = entry
            row += 1
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_traits_tab(self):
        """Setup traits editing tab"""
        canvas = tk.Canvas(self.traits_frame)
        scrollbar = ttk.Scrollbar(self.traits_frame, orient=tk.VERTICAL, command=canvas.scroll)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Info label
        ttk.Label(scrollable_frame, text="Traits & Perks", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=10)
        
        # Traits text area
        ttk.Label(scrollable_frame, text="Current Traits (JSON format):").pack(anchor=tk.W, padx=10)
        self.traits_text = tk.Text(scrollable_frame, height=15, width=50)
        self.traits_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Info frame
        info_frame = ttk.Frame(scrollable_frame)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(info_frame, text="Edit the JSON directly. Common trait keys: 'perks', 'traits', 'status_effects'").pack(anchor=tk.W)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_equipment_tab(self):
        """Setup equipment editing tab"""
        canvas = tk.Canvas(self.equipment_frame)
        scrollbar = ttk.Scrollbar(self.equipment_frame, orient=tk.VERTICAL, command=canvas.scroll)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        ttk.Label(scrollable_frame, text="Equipment", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=10)
        
        self.equipment_text = tk.Text(scrollable_frame, height=20, width=50)
        self.equipment_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(scrollable_frame, text="Edit equipment JSON. Slots: 'weapon', 'armor', 'helmet', 'boots', 'accessory'").pack(anchor=tk.W, padx=10, pady=5)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_inventory_tab(self):
        """Setup inventory editing tab"""
        canvas = tk.Canvas(self.inventory_frame)
        scrollbar = ttk.Scrollbar(self.inventory_frame, orient=tk.VERTICAL, command=canvas.scroll)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        ttk.Label(scrollable_frame, text="Inventory", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=10)
        
        self.inventory_text = tk.Text(scrollable_frame, height=20, width=50)
        self.inventory_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        ttk.Label(scrollable_frame, text="Edit inventory JSON. Format: [{'id': 'item_id', 'quantity': 1}, ...]").pack(anchor=tk.W, padx=10, pady=5)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def open_file(self):
        """Open a save file"""
        filetypes = (("JSON files", "*.json"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(
            title="Select Wartales Save File",
            filetypes=filetypes,
            initialdir=str(Path.home() / "AppData/LocalLow/Shiro Games/Wartales/savegames")
        )
        
        if not filepath:
            return
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            
            self.filepath = filepath
            self.file_label.config(text=f"Loaded: {Path(filepath).name}")
            self.load_characters()
            messagebox.showinfo("Success", "Save file loaded successfully!")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON file")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def load_characters(self):
        """Load characters from the save data"""
        self.char_listbox.delete(0, tk.END)
        self.characters = []
        
        # Try different possible character locations in the JSON
        characters_data = None
        
        if 'characters' in self.data:
            characters_data = self.data['characters']
        elif 'party' in self.data and 'characters' in self.data['party']:
            characters_data = self.data['party']['characters']
        elif 'party' in self.data and 'members' in self.data['party']:
            characters_data = self.data['party']['members']
        
        if characters_data:
            if isinstance(characters_data, list):
                self.characters = characters_data
                for i, char in enumerate(self.characters):
                    name = char.get('name', f'Character {i}')
                    level = char.get('level', '?')
                    self.char_listbox.insert(tk.END, f"{name} (Lvl {level})")
            else:
                messagebox.showwarning("Warning", "Characters data is not in expected format")
        else:
            messagebox.showwarning("Warning", "No characters found in save file")
    
    def on_character_select(self, event):
        """Handle character selection"""
        selection = self.char_listbox.curselection()
        if not selection:
            return
        
        self.current_character = self.characters[selection[0]]
        self.load_character_data()
    
    def load_character_data(self):
        """Load character data into edit fields"""
        if not self.current_character:
            return
        
        # Load stats
        for stat, entry in self.stats_entries.items():
            value = ""
            
            # Check in main character data
            if stat in self.current_character:
                value = str(self.current_character[stat])
            # Check in stats sub-object
            elif 'stats' in self.current_character and stat in self.current_character['stats']:
                value = str(self.current_character['stats'][stat])
            
            entry.delete(0, tk.END)
            entry.insert(0, value)
        
        # Load traits
        traits_data = self.current_character.get('traits', {})
        self.traits_text.delete(1.0, tk.END)
        self.traits_text.insert(1.0, json.dumps(traits_data, indent=2))
        
        # Load equipment
        equipment_data = self.current_character.get('equipment', {})
        self.equipment_text.delete(1.0, tk.END)
        self.equipment_text.insert(1.0, json.dumps(equipment_data, indent=2))
        
        # Load inventory
        inventory_data = self.current_character.get('inventory', [])
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(1.0, json.dumps(inventory_data, indent=2))
    
    def save_file(self):
        """Save changes to the file"""
        if not self.filepath or not self.current_character:
            messagebox.showwarning("Warning", "No file or character selected")
            return
        
        try:
            # Save stats from entries
            for stat, entry in self.stats_entries.items():
                value = entry.get().strip()
                if not value:
                    continue
                
                try:
                    # Try to convert to int
                    value = int(value)
                except ValueError:
                    # Keep as string if not a number
                    pass
                
                # Update in character data
                if stat in self.current_character:
                    self.current_character[stat] = value
                elif 'stats' in self.current_character:
                    self.current_character['stats'][stat] = value
            
            # Save traits
            try:
                traits_text = self.traits_text.get(1.0, tk.END).strip()
                if traits_text:
                    traits_data = json.loads(traits_text)
                    self.current_character['traits'] = traits_data
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON in Traits tab")
                return
            
            # Save equipment
            try:
                equipment_text = self.equipment_text.get(1.0, tk.END).strip()
                if equipment_text:
                    equipment_data = json.loads(equipment_text)
                    self.current_character['equipment'] = equipment_data
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON in Equipment tab")
                return
            
            # Save inventory
            try:
                inventory_text = self.inventory_text.get(1.0, tk.END).strip()
                if inventory_text:
                    inventory_data = json.loads(inventory_text)
                    self.current_character['inventory'] = inventory_data
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON in Inventory tab")
                return
            
            # Write to file
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
            
            messagebox.showinfo("Success", "Save file updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def create_backup(self):
        """Create a backup of the current save file"""
        if not self.filepath:
            messagebox.showwarning("Warning", "No file loaded")
            return
        
        try:
            backup_path = self.filepath + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            shutil.copy2(self.filepath, backup_path)
            messagebox.showinfo("Success", f"Backup created: {Path(backup_path).name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WartalesEditor(root)
    root.mainloop()
