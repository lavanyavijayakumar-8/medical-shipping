import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_store.settings')
django.setup()

from pharmacy.models import Medicine

medicines = [
    # Popular Indian Brand Medicines - Fever & Pain
    {'name': 'Dolo 650', 'description': 'Paracetamol 650mg tablets for fever, headache, body pain, and cold. One of India\'s most trusted fever medicines.', 'price': 1.50, 'stock': 800, 'category': 'Fever & Pain'},
    {'name': 'Crocin Advance', 'description': 'Paracetamol 500mg tablets for quick relief from headache, toothache, body ache, and fever.', 'price': 1.80, 'stock': 700, 'category': 'Fever & Pain'},
    {'name': 'Calpol 500', 'description': 'Paracetamol 500mg for pain and fever relief. Suitable for adults and children above 12.', 'price': 1.60, 'stock': 600, 'category': 'Fever & Pain'},
    {'name': 'Combiflam', 'description': 'Ibuprofen 400mg + Paracetamol 325mg for headache, body pain, toothache, and joint pain.', 'price': 3.50, 'stock': 500, 'category': 'Fever & Pain'},
    {'name': 'Saridon', 'description': 'Triple-action formula with Paracetamol, Propyphenazone, and Caffeine for fast headache relief.', 'price': 2.00, 'stock': 400, 'category': 'Fever & Pain'},
    {'name': 'Disprin', 'description': 'Aspirin 350mg soluble tablets for headache, cold, fever, and mild pain relief.', 'price': 1.20, 'stock': 500, 'category': 'Fever & Pain'},
    {'name': 'Meftal Spas', 'description': 'Mefenamic Acid + Dicyclomine for menstrual cramps, abdominal pain, and spasms.', 'price': 4.50, 'stock': 300, 'category': 'Pain Relief'},
    {'name': 'Volini Spray', 'description': 'Diclofenac-based pain relief spray for muscle pain, back pain, joint pain, and sprains.', 'price': 8.50, 'stock': 250, 'category': 'Pain Relief'},
    {'name': 'Moov Cream', 'description': 'Ayurvedic pain relief cream for back pain, muscle pain, joint pain, and body ache.', 'price': 5.00, 'stock': 350, 'category': 'Pain Relief'},
    {'name': 'Flexon', 'description': 'Ibuprofen 400mg + Paracetamol 325mg for body pain, dental pain, and inflammation.', 'price': 3.00, 'stock': 400, 'category': 'Pain Relief'},

    # Antibiotics (Indian brands)
    {'name': 'Augmentin 625 Duo', 'description': 'Amoxicillin 500mg + Clavulanic Acid 125mg. Broad-spectrum antibiotic for infections.', 'price': 12.00, 'stock': 150, 'category': 'Antibiotic'},
    {'name': 'Azee 500', 'description': 'Azithromycin 500mg antibiotic for respiratory, skin, ear, and throat infections.', 'price': 10.00, 'stock': 200, 'category': 'Antibiotic'},
    {'name': 'Cifran 500', 'description': 'Ciprofloxacin 500mg for urinary tract infections, respiratory infections, and GI infections.', 'price': 8.00, 'stock': 180, 'category': 'Antibiotic'},
    {'name': 'Taxim-O 200', 'description': 'Cefixime 200mg antibiotic for typhoid, UTI, respiratory tract, and ear infections.', 'price': 9.50, 'stock': 160, 'category': 'Antibiotic'},
    {'name': 'Ciplox 500', 'description': 'Ciprofloxacin 500mg for bacterial infections of lungs, skin, bones, and joints.', 'price': 7.50, 'stock': 170, 'category': 'Antibiotic'},

    # Cough & Cold
    {'name': 'Benadryl Cough Syrup', 'description': 'Diphenhydramine-based cough syrup for dry cough, throat irritation, and allergic cough.', 'price': 6.00, 'stock': 300, 'category': 'Cough & Cold'},
    {'name': 'Vicks Action 500', 'description': 'Paracetamol + Phenylephrine + Caffeine for cold, headache, body pain, and blocked nose.', 'price': 2.50, 'stock': 450, 'category': 'Cough & Cold'},
    {'name': 'Sinarest', 'description': 'Paracetamol + Chlorpheniramine + Pseudoephedrine for cold, flu, and sinus congestion.', 'price': 3.00, 'stock': 350, 'category': 'Cough & Cold'},
    {'name': 'Cheston Cold', 'description': 'Cetirizine + Paracetamol + Phenylephrine for cold, sneezing, runny nose, and body ache.', 'price': 3.50, 'stock': 300, 'category': 'Cough & Cold'},
    {'name': 'Honitus Cough Syrup', 'description': 'Dabur herbal cough syrup with Tulsi, Mulethi, and Honey for natural cough relief.', 'price': 4.00, 'stock': 250, 'category': 'Cough & Cold'},
    {'name': 'Corex-D Syrup', 'description': 'Dextromethorphan + Chlorpheniramine syrup for dry cough and allergic cough.', 'price': 5.50, 'stock': 200, 'category': 'Cough & Cold'},
    {'name': 'Otrivin Nasal Drops', 'description': 'Xylometazoline nasal drops for instant relief from blocked and stuffy nose.', 'price': 3.00, 'stock': 300, 'category': 'Cough & Cold'},

    # Digestive & Antacid
    {'name': 'Gelusil MPS', 'description': 'Antacid with Magnesium + Aluminium Hydroxide + Simethicone for acidity, gas, and heartburn.', 'price': 3.00, 'stock': 400, 'category': 'Antacid'},
    {'name': 'Digene', 'description': 'Antacid gel for acidity, gas, bloating, and stomach discomfort. Mint flavour.', 'price': 4.00, 'stock': 350, 'category': 'Antacid'},
    {'name': 'Eno', 'description': 'Fast-acting antacid powder for instant relief from acidity and stomach gas.', 'price': 1.00, 'stock': 600, 'category': 'Antacid'},
    {'name': 'Pan-D', 'description': 'Pantoprazole 40mg + Domperidone 30mg for acid reflux, GERD, and gastric ulcers.', 'price': 6.00, 'stock': 200, 'category': 'Antacid'},
    {'name': 'Pudin Hara', 'description': 'Mint-based digestive capsules for indigestion, gas, acidity, and stomach ache.', 'price': 2.00, 'stock': 500, 'category': 'Digestive'},
    {'name': 'Dabur Hajmola', 'description': 'Ayurvedic digestive tablets for indigestion and to improve appetite. Multiple flavours.', 'price': 1.50, 'stock': 600, 'category': 'Digestive'},
    {'name': 'Cyclopam', 'description': 'Dicyclomine + Paracetamol for abdominal cramps, spasms, and stomach pain.', 'price': 4.00, 'stock': 250, 'category': 'Digestive'},
    {'name': 'Norflox TZ', 'description': 'Norfloxacin + Tinidazole for loose motions, diarrhea, and stomach infections.', 'price': 5.00, 'stock': 200, 'category': 'Digestive'},
    {'name': 'Econorm Sachet', 'description': 'Saccharomyces boulardii probiotic for diarrhea, IBS, and restoring gut flora.', 'price': 3.50, 'stock': 300, 'category': 'Digestive'},

    # Diabetes
    {'name': 'Glycomet 500', 'description': 'Metformin 500mg for type 2 diabetes management. Helps control blood sugar levels.', 'price': 3.00, 'stock': 300, 'category': 'Diabetes'},
    {'name': 'Glucobay 50', 'description': 'Acarbose 50mg for controlling post-meal blood sugar spikes in type 2 diabetes.', 'price': 5.00, 'stock': 200, 'category': 'Diabetes'},
    {'name': 'Janumet 50/500', 'description': 'Sitagliptin + Metformin for improved blood sugar control in type 2 diabetes.', 'price': 15.00, 'stock': 100, 'category': 'Diabetes'},
    {'name': 'Amaryl M 2mg', 'description': 'Glimepiride + Metformin combination for effective type 2 diabetes management.', 'price': 8.00, 'stock': 150, 'category': 'Diabetes'},

    # Blood Pressure & Heart
    {'name': 'Amlokind 5', 'description': 'Amlodipine 5mg for high blood pressure and chest pain (angina).', 'price': 4.00, 'stock': 250, 'category': 'Blood Pressure'},
    {'name': 'Telma 40', 'description': 'Telmisartan 40mg for hypertension and cardiovascular protection.', 'price': 6.00, 'stock': 200, 'category': 'Blood Pressure'},
    {'name': 'Ecosprin 75', 'description': 'Aspirin 75mg for blood thinning, heart attack and stroke prevention.', 'price': 2.00, 'stock': 400, 'category': 'Heart'},
    {'name': 'Clopitab 75', 'description': 'Clopidogrel 75mg antiplatelet tablet for prevention of heart attack and stroke.', 'price': 5.00, 'stock': 200, 'category': 'Heart'},
    {'name': 'Aten 50', 'description': 'Atenolol 50mg beta-blocker for high blood pressure and chest pain.', 'price': 3.50, 'stock': 250, 'category': 'Blood Pressure'},

    # Allergy
    {'name': 'Cetrizine (Cetzine)', 'description': 'Cetirizine 10mg for allergies, hay fever, sneezing, runny nose, and itchy eyes.', 'price': 2.00, 'stock': 500, 'category': 'Allergy'},
    {'name': 'Allegra 120', 'description': 'Fexofenadine 120mg for seasonal allergies, sneezing, and chronic urticaria.', 'price': 6.00, 'stock': 250, 'category': 'Allergy'},
    {'name': 'Montair LC', 'description': 'Montelukast + Levocetirizine for allergic rhinitis, asthma, and breathing difficulties.', 'price': 7.00, 'stock': 200, 'category': 'Allergy'},
    {'name': 'Avil 25', 'description': 'Pheniramine 25mg antihistamine for allergic reactions, itching, and hives.', 'price': 1.50, 'stock': 400, 'category': 'Allergy'},

    # Vitamins & Supplements
    {'name': 'Becosules Capsule', 'description': 'B-complex vitamin capsule with Vitamin C for mouth ulcers, weakness, and overall health.', 'price': 2.50, 'stock': 500, 'category': 'Vitamins'},
    {'name': 'Supradyn', 'description': 'Complete multivitamin with minerals for daily energy, immunity, and overall well-being.', 'price': 5.00, 'stock': 350, 'category': 'Vitamins'},
    {'name': 'Zincovit', 'description': 'Multivitamin with Zinc, Selenium, and antioxidants for immunity and recovery.', 'price': 4.00, 'stock': 300, 'category': 'Vitamins'},
    {'name': 'Shelcal 500', 'description': 'Calcium 500mg + Vitamin D3 for strong bones, teeth, and prevention of osteoporosis.', 'price': 3.50, 'stock': 400, 'category': 'Vitamins'},
    {'name': 'Limcee Vitamin C', 'description': 'Vitamin C 500mg chewable tablets for immunity, skin health, and antioxidant support.', 'price': 1.50, 'stock': 600, 'category': 'Vitamins'},
    {'name': 'Revital H', 'description': 'Daily health supplement with Ginseng, vitamins, and minerals for energy and stamina.', 'price': 8.00, 'stock': 250, 'category': 'Supplements'},
    {'name': 'Neurobion Forte', 'description': 'Vitamin B1, B6, B12 combination for nerve health, tingling, numbness, and weakness.', 'price': 3.00, 'stock': 350, 'category': 'Vitamins'},
    {'name': 'Evion 400', 'description': 'Vitamin E 400mg capsule for skin health, hair growth, and antioxidant protection.', 'price': 2.50, 'stock': 400, 'category': 'Vitamins'},

    # Skin Care
    {'name': 'Betadine Ointment', 'description': 'Povidone-iodine antiseptic ointment for cuts, wounds, burns, and skin infections.', 'price': 4.00, 'stock': 300, 'category': 'Skin Care'},
    {'name': 'Soframycin Cream', 'description': 'Framycetin antibiotic cream for minor cuts, burns, wounds, and skin infections.', 'price': 3.50, 'stock': 250, 'category': 'Skin Care'},
    {'name': 'Candid Cream', 'description': 'Clotrimazole antifungal cream for ringworm, athlete foot, and fungal skin infections.', 'price': 5.00, 'stock': 200, 'category': 'Skin Care'},
    {'name': 'Boroline Cream', 'description': 'Antiseptic ayurvedic cream for dry skin, cracked heels, and minor cuts.', 'price': 2.00, 'stock': 400, 'category': 'Skin Care'},
    {'name': 'Lacto Calamine', 'description': 'Calamine lotion with kaolin for oily skin, pimples, sunburn, and skin soothing.', 'price': 4.50, 'stock': 300, 'category': 'Skin Care'},

    # Eye & Ear Care
    {'name': 'Itone Eye Drops', 'description': 'Ayurvedic eye drops for eye strain, dryness, redness, and irritation.', 'price': 3.00, 'stock': 250, 'category': 'Eye Care'},
    {'name': 'Genteal Eye Drops', 'description': 'Hydroxypropyl methylcellulose lubricant eye drops for dry eyes and irritation.', 'price': 5.00, 'stock': 200, 'category': 'Eye Care'},
    {'name': 'Otogesic Ear Drops', 'description': 'Analgesic ear drops for earache, ear infection pain, and inflammation.', 'price': 4.00, 'stock': 150, 'category': 'Ear Care'},

    # First Aid
    {'name': 'Dettol Antiseptic', 'description': 'Chloroxylenol antiseptic liquid for wound cleaning, bathing, and surface disinfection.', 'price': 5.00, 'stock': 400, 'category': 'First Aid'},
    {'name': 'Band-Aid Strips', 'description': 'Adhesive bandage strips for minor cuts, scrapes, and small wounds. Waterproof.', 'price': 2.50, 'stock': 500, 'category': 'First Aid'},
    {'name': 'Burnol Cream', 'description': 'Antiseptic burn cream for minor burns, scalds, and sunburn relief.', 'price': 3.00, 'stock': 300, 'category': 'First Aid'},
    {'name': 'ORS Electral Powder', 'description': 'WHO-formula oral rehydration salts for dehydration from diarrhea, vomiting, or heat.', 'price': 1.00, 'stock': 700, 'category': 'First Aid'},
    {'name': 'Cotton Roll (Surgical)', 'description': 'Absorbent surgical cotton roll for wound dressing, cleaning, and first aid.', 'price': 2.00, 'stock': 500, 'category': 'First Aid'},

    # Thyroid
    {'name': 'Thyronorm 50mcg', 'description': 'Levothyroxine 50mcg for hypothyroidism and thyroid hormone replacement therapy.', 'price': 3.00, 'stock': 300, 'category': 'Thyroid'},
    {'name': 'Eltroxin 100mcg', 'description': 'Levothyroxine 100mcg for underactive thyroid (hypothyroidism) management.', 'price': 4.00, 'stock': 250, 'category': 'Thyroid'},

    # Bone & Joint
    {'name': 'Caldikind Plus', 'description': 'Calcium + Vitamin D3 + Zinc for bone strength, joint health, and osteoporosis prevention.', 'price': 5.00, 'stock': 250, 'category': 'Bone & Joint'},
    {'name': 'Ostocalcium', 'description': 'Calcium supplement with Vitamin D for strong bones and teeth. Suitable for all ages.', 'price': 4.50, 'stock': 300, 'category': 'Bone & Joint'},

    # Women Health
    {'name': 'Folvite 5mg', 'description': 'Folic acid supplement essential during pregnancy for baby brain and spine development.', 'price': 1.50, 'stock': 400, 'category': 'Women Health'},
    {'name': 'Autrin', 'description': 'Iron + Folic acid + Vitamin B12 capsule for anemia treatment during pregnancy.', 'price': 3.00, 'stock': 300, 'category': 'Women Health'},
    {'name': 'i-Pill', 'description': 'Levonorgestrel 1.5mg emergency contraceptive pill. To be taken within 72 hours.', 'price': 2.50, 'stock': 200, 'category': 'Women Health'},
]

def seed():
    count = 0
    for data in medicines:
        _, created = Medicine.objects.get_or_create(name=data['name'], defaults=data)
        if created:
            count += 1
    print(f"Seeding complete. {count} new medicines added. Total: {Medicine.objects.count()}")

if __name__ == '__main__':
    seed()
