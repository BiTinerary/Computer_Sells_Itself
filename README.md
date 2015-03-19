# Laptop_Sells_Itself
Preface: Implement the following into BLDZR/Hardware Tester. After Hardware testing checks out, end-user will be prompted for quality verification.

Script to collect specs then generate CL/Ebay/Amazon listing.

The various commands for gathering basic consumer specifications of the
current machine. This info is then appended to a text file (hardcoded as
welp.txt) on the current users Desktop.

For future reference: Create a selenium script that posts to CraigsList, Amazon, and/or Ebay using the generated text to fill in the descriptions, where necessary. This process will be similar to your Auto_Amazon_Lister repository. Otherwise simply use Make/Model to find the item on Amazon and add to their preconfigured product catalog.

Epilogue: After the listing has been generated (and/or before) it should be cross referenced with "master list file". If it matches up then the quantity is simply 1 upped. This only really applies to Amazon where all listings (Quality, Store, supplier) for the same item are allocated and terms of service might be "breached" if multiple listings are created for the same item. As opposed to one listing, one supplier with multiple quantities. Consider implementing this feature later one and working on the Ebay, Craigslist side of things for now.
