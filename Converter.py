import nbtlib, os, re, datetime

class DatToTxtConversion:
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.player_data = None

    def get_input_output_folders(self):
        print('Please provide the full path to the folder containing the .dat files to be converted.\nE.g. "C:/Users/JohnSmith/Documents/datFiles".')
        self.input_folder = input('Path to folder: ').strip('" ')
        print('\nPath to .dat folder is ' + self.input_folder)

        print('\nPlease provide the full path to the folder the converted .txt files should output to.\nE.g. "C:/Users/JohnSmith/Documents/txtFiles".')
        self.output_folder = input('Path to folder: ').strip('" ')
        print('\nPath to .txt output folder is ' + self.output_folder)

    def find_dat_files(self):
        dat_files = []

        for file in os.listdir(self.input_folder):
            if file.endswith('.dat'):
                dat_files.append(os.path.join(self.input_folder, file))

        return dat_files

    @staticmethod
    def convert_dat_to_txt(dat_file_path):
        try:
            dat_file = nbtlib.load(dat_file_path)
            if not isinstance(dat_file, nbtlib.Compound):
                raise TypeError("Expected a Compound root tag in the NBT file.")
            return repr(dat_file)
        except TypeError as e:
            print(f"Error processing {dat_file_path}: {e}")
        except EOFError as e:
            print(f"Error processing {dat_file_path}: {e}")

    @staticmethod
    def extract_player_data(raw_data):

        try:
            player_name = re.findall(r"'lastKnownName': String\('([^']*)'\)", raw_data)[0].strip("[']")
        except IndexError:
            print('Player name index error.')
            player_name = None
        except TypeError:
            print('Player name type error.')
            player_name = None

        try:
            dimension = re.findall(r"'Dimension': String\('([^']*)'\)", raw_data)[0].strip("[']")
        except IndexError:
            print('Dimension index error.')
            dimension = None
        except TypeError:
            print('Dimension type error.')
            dimension = None

        try:
            pos = re.findall(r"'Pos': List\[Double]\(\[Double\(([-\d.]+)\), Double\(([-\d.]+)\), Double\(([-\d.]+)\)]\)", raw_data)[0]
        except IndexError:
            print('Position index error.')
            pos = None
        except TypeError:
            print('Position type error.')
            pos = None

        try:
            last_played = datetime.datetime.fromtimestamp(float(re.findall(r"'lastPlayed': Long\((\d+)\)", raw_data)[0]) / 1000).strftime('%Y-%m-%d %H:%M')
        except IndexError:
            print('Last played index error.')
            last_played = None
        except TypeError:
            print('Last played type error.')
            last_played = None

        try:
            death_dimension = re.findall(r"'dimension': String\('([^']*)'\)", raw_data)[0].strip("[']")
        except IndexError:
            print('Death dimension index error.')
            death_dimension = None
        except TypeError:
            print('Death dimension type error.')
            death_dimension = None

        try:
            death_pos = re.findall(r"'LastDeathLocation': Compound\(\{'pos': IntArray\(\[Int\(([-\d]+)\), Int\(([-\d]+)\), Int\(([-\d]+)\)]\)", raw_data)[0]
        except IndexError:
            print('Death position index error.')
            death_pos = None
        except TypeError:
            print('Death position type error.')
            death_pos = None

        try:
            paper_origin_pos = re.findall(r"'Paper.Origin': List\[Double]\(\[Double\(([-\d.]+)\), Double\(([-\d.]+)\), Double\(([-\d.]+)\)]\)",raw_data)[0]
        except IndexError:
            print('Paper origin position index error.')
            paper_origin_pos = None
        except TypeError:
            print('Paper origin position type error.')
            paper_origin_pos = None

        try:
            inventory = re.findall(r"'Inventory':\s*List\[Compound]\((\[.*?])\), 'UUID':", raw_data, re.DOTALL)[0].strip("[']")
            inventory = inventory.replace(',', '\n')
            inventory = inventory.replace('Byte(', '')
            inventory = inventory.replace('Compound', '')
            inventory = inventory.replace(')', '')
            inventory = inventory.replace('(', '')
            inventory = inventory.replace('}', '')
            inventory = inventory.replace('{', '')
            inventory = inventory.replace(']', '')
            inventory = inventory.replace('[', '')
            inventory = inventory.replace('Int', '')
            inventory = inventory.replace("'", "")
            inventory = inventory.replace('String', '')
            inventory = inventory.replace("count:", "\ncount:")
            inventory = inventory.replace("components: ", "")
            inventory = inventory.replace("levels: ", "\n levels:\n ")
            inventory = inventory.replace(" Slot", "slot")
            inventory = inventory.replace(" minecraft", "  minecraft")
            inventory = inventory.replace("  minecraft:enchantments:", "minecraft:enchantments:")
            inventory = inventory.replace("  minecraft:custom_name:", "minecraft:custom_name:")
            inventory = inventory.replace("  minecraft:repair_cost:", "minecraft:repair_cost:")
            inventory = inventory.replace("  minecraft:damage:", "minecraft:damage:")
            inventory = inventory.replace(" id:", "id:")
            inventory = inventory.replace("  lore:", "lore:")
            inventory = inventory.replace("id:  minecraft:", "id: minecraft:")
            inventory = inventory.replace('"text":', ' text:')
            inventory = inventory.replace('"color":', ' color:')
            inventory = inventory.replace('"italic":', ' italic:')
            inventory = inventory.replace('"underlined":', ' underlined:')
            inventory = inventory.replace('"obfuscated":', ' obfuscated:')
            inventory = inventory.replace('"strikethrough":', ' strikethrough:')
            inventory = inventory.replace('"extra":"bold":', '\n extra:\n bold:')
            inventory = inventory.replace('"bold":', ' bold:')
            inventory = inventory.replace('"extra":', '\n extra:')
            inventory = inventory.replace('minecraft:', '')
        except IndexError:
            print('Inventory index error.')
            inventory = None
        except TypeError:
            print('Inventory origin position type error.')
            inventory = None

        try:
            enderchest = re.findall(r"'EnderItems':\s*List\[Compound]\((\[.*?])\)", raw_data, re.DOTALL)[0].strip("[']")
            enderchest = enderchest.replace(',', '\n')
            enderchest = enderchest.replace('Byte(', '')
            enderchest = enderchest.replace('Compound', '')
            enderchest = enderchest.replace(')', '')
            enderchest = enderchest.replace('(', '')
            enderchest = enderchest.replace('}', '')
            enderchest = enderchest.replace('{', '')
            enderchest = enderchest.replace(']', '')
            enderchest = enderchest.replace('[', '')
            enderchest = enderchest.replace('Int', '')
            enderchest = enderchest.replace("'", "")
            enderchest = enderchest.replace('String', '')
            enderchest = enderchest.replace("count:", "\ncount:")
            enderchest = enderchest.replace("components: ", "")
            enderchest = enderchest.replace("levels: ", "\n levels:\n ")
            enderchest = enderchest.replace(" Slot", "slot")
            enderchest = enderchest.replace(" minecraft", "  minecraft")
            enderchest = enderchest.replace("  minecraft:enchantments:", "minecraft:enchantments:")
            enderchest = enderchest.replace("  minecraft:custom_name:", "minecraft:custom_name:")
            enderchest = enderchest.replace("  minecraft:repair_cost:", "minecraft:repair_cost:")
            enderchest = enderchest.replace("  minecraft:damage:", "minecraft:damage:")
            enderchest = enderchest.replace(" id:", "id:")
            enderchest = enderchest.replace("  lore:", "lore:")
            enderchest = enderchest.replace("id:  minecraft:", "id: minecraft:")
            enderchest = enderchest.replace('"text":', ' text:')
            enderchest = enderchest.replace('"color":', ' color:')
            enderchest = enderchest.replace('"italic":', ' italic:')
            enderchest = enderchest.replace('"underlined":', ' underlined:')
            enderchest = enderchest.replace('"obfuscated":', ' obfuscated:')
            enderchest = enderchest.replace('"strikethrough":', ' strikethrough:')
            enderchest = enderchest.replace('"extra":"bold":', '\n extra:\n bold:')
            enderchest = enderchest.replace('"bold":', ' bold:')
            enderchest = enderchest.replace('"extra":', '\n extra:')
            enderchest = enderchest.replace('minecraft:', '')
        except IndexError:
            print('Enderchest index error.')
            enderchest = None
        except TypeError:
            print('Enderchest origin position type error.')
            enderchest = None

        return {
            "player_name": player_name,
            "dimension": dimension,
            "position": pos,
            "last_played": last_played,
            "death_dimension": death_dimension,
            "death_pos": death_pos,
            "paper_origin_pos": paper_origin_pos,
            "inventory": inventory,
            "enderchest": enderchest
        }

    @staticmethod
    def sanitise_filename(filename):
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    def save_player_data_txt(self, player_data, dat_file_path):
        if player_data["player_name"]:
            txt_file_name = f"{player_data['player_name']}.txt"
        else:
            txt_file_name = "unknown_player.txt"

        txt_file_path = os.path.join(self.output_folder, self.sanitise_filename(txt_file_name))

        with open(txt_file_path, 'w', encoding='utf=8') as dat_txt_file:
            dat_txt_file.write(f"Original file: {dat_file_path}\n")
            dat_txt_file.write(f"Player Name: {player_data['player_name']}\n")
            dat_txt_file.write(f"Dimension: {player_data['dimension']}\n")
            dat_txt_file.write(f"Position: {player_data['position']}\n")
            dat_txt_file.write(f"Last Played: {player_data['last_played']}\n")
            dat_txt_file.write(f"Death Dimension: {player_data['death_dimension']}\n")
            dat_txt_file.write(f"Death Position: {player_data['death_pos']}\n")
            dat_txt_file.write(f"Paper Origin Position: {player_data['paper_origin_pos']}\n\n")
            dat_txt_file.write(f"Inventory: {player_data['inventory']}\n\n")
            dat_txt_file.write(f"Enderchest: {player_data['enderchest']}")

            print(f'Saving file: {txt_file_path}')

def main():
    conversion = DatToTxtConversion()
    conversion.get_input_output_folders()
    dat_files = conversion.find_dat_files()

    if not dat_files:
        print("No .dat files were found in the input folder specified.")

    for dat_file_path in dat_files:
        print(f"Processing file: {dat_file_path}")
        raw_data = conversion.convert_dat_to_txt(dat_file_path)
        player_data = conversion.extract_player_data(raw_data)
        conversion.save_player_data_txt(player_data, dat_file_path)

if __name__ == '__main__':
    main()
    print('\n')
    input('Press enter to exit.')