#!/usr/bin/env python3
"""Generate the English SEO feature guides for the static GitHub Pages site."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP_STORE = "https://apps.apple.com/app/id6752308731"


FEATURES = {
    "scan-to-pdf": {
        "title": "Scan to PDF on iPhone and iPad | ProScan PDF",
        "description": "Scan documents, receipts, IDs, photos and whiteboards to clean PDFs on iPhone or iPad. Eight scan modes, page sizes and offline processing.",
        "eyebrow": "A focused mobile scanner",
        "heading": "Scan to PDF.\nKeep every page clear.",
        "lead": "Turn paper documents into polished PDF files with eight purpose-built scanning modes, practical page settings and Apple’s familiar capture interface.",
        "image": "screen-scan",
        "image_alt": "Document positioned in the ProScan PDF scanning interface",
        "icon": "document",
        "callout_title": "Eight scan modes",
        "callout_text": "Choose the mode that fits the page.",
        "chips": ["Documents", "Receipts", "IDs", "Works offline"],
        "proofs": [
            ("auto", "The right mode for the page", "Choose Document, Auto, Receipt, ID, Photo, Form, B&W Text or Whiteboard before capture. Each option keeps the setup understandable instead of hiding everything behind one generic scanner."),
            ("pages", "Set up the PDF first", "Select A4, Letter, Legal or another supported page size, choose portrait or landscape, and decide whether page numbers or timestamps should appear in the finished document."),
            ("lock", "Local by design", "Core scanning and PDF creation happen on your iPhone or iPad. Your document is not uploaded to a ProScan PDF server for processing."),
        ],
        "steps": [
            ("Choose a scanning mode", "Start from Home and select the mode that best describes the page. Auto is useful for general capture, while Receipt, ID, Form, B&W Text and Whiteboard make the intended result clear before you begin."),
            ("Capture one or more pages", "Use Apple’s document scanning interface to frame the page, control flash and filters, and switch between automatic and manual shutter behavior. Review each capture and add more pages when the document continues."),
            ("Finish and save the PDF", "Tap Finish after the last page. ProScan PDF creates the document in My Files, keeps a local copy ready for fast access and can create a private iCloud backup when iCloud is available."),
        ],
        "details": [
            ("A setup that matches real paperwork", "A receipt does not need the same treatment as a whiteboard or an identity document. Dedicated modes make the choice visible, while page size, orientation, numbering and timestamps remain available in one compact Scan Setup area."),
            ("Multi-page scanning without extra steps", "Capture a single page or continue building a longer document in the same scan. The resulting pages stay together in one PDF, ready to view, rename, organize, sign, lock, compress or share from the library."),
            ("Designed for a dependable handoff", "A successful save is confirmed on screen, and the finished PDF appears in My Files. Local-first storage avoids waiting for an iCloud download every time you reopen a recent document, while optional backup helps when moving to another Apple device."),
        ],
        "note_title": "About the camera controls",
        "note": "The capture screen is Apple’s native document-scanner interface. Its shutter, flash, filter, review and Auto/Manual controls can vary slightly between iOS versions, but ProScan PDF keeps the surrounding scan mode, PDF setup, save flow and document library consistent.",
        "faqs": [
            ("Can I scan more than one page into the same PDF?", "Yes. Continue capturing pages before you tap Finish, and ProScan PDF saves them together as one multi-page PDF."),
            ("Which scan modes are available?", "Document, Auto, Receipt, ID, Photo, Form, B&W Text and Whiteboard are available from the Home screen."),
            ("Can scanning work without an internet connection?", "Core capture and PDF creation work on the device. Sharing and iCloud backup require a connection when you choose to use them."),
            ("Where does the finished scan appear?", "After you tap Finish and the save succeeds, the PDF appears in My Files with a local copy available for fast access."),
        ],
        "related": ["photo-to-pdf", "ocr-text-extraction", "organize-pdf-pages", "sign-pdf"],
    },
    "photo-to-pdf": {
        "title": "Convert Photos to PDF on iPhone and iPad | ProScan PDF",
        "description": "Turn one photo or a group of images into a polished PDF on iPhone or iPad. Private on-device conversion with no ads or watermarks.",
        "eyebrow": "Photos become one document",
        "heading": "Photos to PDF.\nOne clean file.",
        "lead": "Choose one or more images and turn them into a PDF that is easier to file, send and revisit than a loose group of photos.",
        "image": "screen-tools",
        "image_alt": "Photos to PDF tool in ProScan PDF",
        "icon": "images",
        "callout_title": "One or many photos",
        "callout_text": "Create a shareable PDF locally.",
        "chips": ["Multiple photos", "PDF output", "No watermark", "On-device"],
        "proofs": [
            ("images", "A simpler way to send images", "Combine related photos into one PDF instead of attaching each image separately. It is useful for photographed notes, records, receipts, artwork, reference pages and other visual material."),
            ("document", "A document-shaped result", "The PDF keeps every selected image as a page inside one file, making the result easier to rename, store, organize and share from the same My Files library as your scans."),
            ("lock", "Private conversion", "Photo processing and PDF creation happen on the device. ProScan PDF does not need to upload the selected images to its own server to build the file."),
        ],
        "steps": [
            ("Open Photos to PDF", "Go to Tools and choose Photos to PDF. The system photo picker lets you select the images you want to include without granting unnecessary access to the rest of your library."),
            ("Select the source photos", "Choose a single photo for a quick one-page PDF or select multiple related images for a longer document. ProScan PDF prepares each image as a PDF page without stretching its proportions."),
            ("Create and continue in My Files", "Save the result and continue working from My Files. You can rename it, view it, organize pages, compress it, add a watermark, lock it with a password or share it."),
        ],
        "details": [
            ("Useful beyond traditional scanning", "Photos to PDF works well when the source is already in your Photos library: screenshots, downloaded forms, photographed handwritten notes, reference images or a sequence of pages captured earlier."),
            ("Keeps the workflow in one place", "The generated PDF joins the same document library as scanned files. There is no need to move between a photo converter, a PDF editor and a sharing utility just to finish one document."),
            ("No ads and no automatic watermark", "The app does not interrupt the conversion with advertising and does not stamp the result with a ProScan PDF watermark. If you want a watermark, the separate Add Watermark tool lets you choose the text and color intentionally."),
        ],
        "note_title": "Image quality and file size",
        "note": "High-resolution photos can produce a larger PDF. If the finished file is too large for email or storage, use Compress PDF afterward. Compression is most effective for image-based documents such as PDFs created from photos.",
        "faqs": [
            ("Can I convert several photos into one PDF?", "Yes. Select multiple photos and ProScan PDF creates a multi-page PDF with one selected image on each page."),
            ("Does the app stretch imported photos?", "No. The conversion preserves the photo’s proportions instead of forcing it into a distorted shape."),
            ("Will ProScan PDF add a watermark?", "No automatic watermark is added. The separate watermark tool is available only when you want to apply one yourself."),
            ("Can I compress the PDF afterward?", "Yes. Open Compress PDF from Tools to reduce the size of image-based PDFs when a smaller file is needed."),
        ],
        "related": ["scan-to-pdf", "pdf-to-images", "pdf-compressor", "organize-pdf-pages"],
    },
    "pdf-to-images": {
        "title": "Convert PDF to JPG Images on iPhone | ProScan PDF",
        "description": "Convert every PDF page to a high-quality JPG on iPhone or iPad. Save images to Photos, share them or save them to Files with on-device processing.",
        "eyebrow": "Every PDF page becomes an image",
        "heading": "PDF to Images.\nSave every page.",
        "lead": "Turn each page of a PDF into a separate high-quality JPG, then choose whether to save the images to Photos or share them with another app.",
        "image": "screen-tools",
        "image_alt": "PDF to Images tool on the ProScan PDF tools screen",
        "icon": "photo",
        "callout_title": "One JPG per page",
        "callout_text": "Save to Photos, Files or another app.",
        "chips": ["JPG output", "One image per page", "Save or share", "On-device"],
        "proofs": [
            ("photo", "A clear image for every page", "ProScan PDF renders the complete PDF in page order and creates one high-quality JPG for each page. Multi-page documents become an organized set of numbered image files."),
            ("images", "Choose where the result goes", "When the images are ready, save them directly to Photos or open the iOS share sheet to send them, save them to Files or continue in another compatible app."),
            ("lock", "Private conversion", "The PDF is rendered locally on your iPhone or iPad. ProScan PDF does not upload the document to its own conversion server."),
        ],
        "steps": [
            ("Choose the source PDF", "Open Tools, tap PDF to Images and select a document from My Files. The app confirms the selected source before beginning the export."),
            ("Create the page images", "ProScan PDF renders each readable page locally and creates sequentially numbered JPG files so their original order remains clear."),
            ("Save or share the result", "Choose Save to Photos for direct photo-library access, or choose Share or Save to Files to use the standard iOS share sheet. A completion card confirms a successful save to Photos."),
        ],
        "details": [
            ("Useful when a PDF is not the required format", "Image export is practical for uploading individual pages to a form, placing a PDF page in a presentation, sending one page through a messaging app or keeping visual copies in Photos."),
            ("Page order remains understandable", "Every image filename includes its page number. A five-page PDF produces five JPG files in the same sequence as the source rather than one long or combined image."),
            ("Temporary files are cleaned up", "The page images are prepared in temporary app storage for the save or share action. After the workflow finishes, ProScan PDF removes the temporary export instead of leaving hidden duplicate files behind."),
        ],
        "note_title": "Large documents need more time and memory",
        "note": "Each PDF page must be rendered as a full image, so a long or graphics-heavy document can take longer and use more temporary memory. Password-locked PDFs must be unlocked before they can be exported. The source PDF remains unchanged.",
        "faqs": [
            ("Which image format does PDF to Images create?", "The tool creates a separate high-quality JPG file for every PDF page."),
            ("Can I export a multi-page PDF?", "Yes. Every readable page is exported in order with a numbered filename."),
            ("Can I save the images somewhere other than Photos?", "Yes. Choose Share or Save to Files to open the standard iOS share sheet and select an available destination."),
            ("Does the PDF leave my device for conversion?", "No. Page rendering and JPG creation happen locally on your iPhone or iPad."),
        ],
        "related": ["photo-to-pdf", "ocr-text-extraction", "pdf-compressor", "organize-pdf-pages"],
    },
    "add-watermark": {
        "title": "Add a Text Watermark to PDF on iPhone | ProScan PDF",
        "description": "Add a diagonal text watermark to every PDF page on iPhone or iPad. Choose from seven colors and save a separate watermarked copy entirely on-device.",
        "eyebrow": "Mark every page intentionally",
        "heading": "Add a watermark.\nKeep the original.",
        "lead": "Apply your own semi-transparent text across every page, choose a color that suits the document and save the result as a separate PDF copy.",
        "image": "screen-tools",
        "image_alt": "Add Watermark tool on the ProScan PDF tools screen",
        "icon": "watermark",
        "callout_title": "Text and color control",
        "callout_text": "Seven colors, one protected original.",
        "chips": ["Custom text", "Seven colors", "Every page", "New PDF copy"],
        "proofs": [
            ("watermark", "Your message across the document", "Enter text such as CONFIDENTIAL, DRAFT, SAMPLE or a project name. ProScan PDF places the message diagonally across the center of every page with a readable semi-transparent finish."),
            ("auto", "Choose a suitable color", "Select Cyan, White, Light Gray, Dark Gray, Dark Red, Dark Yellow or Black. Cyan is selected by default, and the color choice remains explicit before the PDF is created."),
            ("document", "A separate watermarked copy", "The source PDF is not silently overwritten. ProScan PDF creates a new watermarked file in My Files so the untouched original remains available."),
        ],
        "steps": [
            ("Select the PDF", "Open Tools, choose Add Watermark and select the PDF you want to mark from My Files."),
            ("Enter text and choose a color", "Replace the default CONFIDENTIAL text with your own wording if needed, then select one of the seven available colors."),
            ("Create the watermarked copy", "Tap Create Watermarked PDF. The document is processed locally, saved to My Files as a new PDF and followed by a completion confirmation."),
        ],
        "details": [
            ("Consistent placement on every page", "The watermark is sized relative to each PDF page and placed diagonally through the center, creating a consistent visual treatment across portrait, landscape and mixed-size documents."),
            ("Useful for drafts and controlled sharing", "A visible watermark can identify a draft, label a sample, mark internal material or add a project or organization name before the PDF is sent to someone else."),
            ("Works with the rest of the PDF toolkit", "The new copy appears in My Files and can then be renamed, organized, compressed, signed, locked or shared without leaving ProScan PDF."),
        ],
        "note_title": "Keep the source when editable text matters",
        "note": "The watermark workflow rebuilds the PDF page by page to place the text consistently. Keep the original for archival use or when selectable text, annotations or vector content must remain untouched. The separate-copy workflow makes that easy.",
        "faqs": [
            ("Is the watermark added to every page?", "Yes. The selected text and color are applied across every page in the new PDF copy."),
            ("Which watermark colors are available?", "Cyan, White, Light Gray, Dark Gray, Dark Red, Dark Yellow and Black are available, with Cyan selected by default."),
            ("Will the tool replace my original PDF?", "No. ProScan PDF saves a separate watermarked copy in My Files."),
            ("Is the PDF uploaded for watermarking?", "No. The watermark is rendered locally on your iPhone or iPad."),
        ],
        "related": ["pdf-compressor", "sign-pdf", "organize-pdf-pages", "photo-to-pdf"],
    },
    "pdf-compressor": {
        "title": "Compress PDF Files on iPhone and iPad | ProScan PDF",
        "description": "Compress scanned and image-based PDFs locally on iPhone or iPad. See the original size, compressed size and percentage reduction before continuing.",
        "eyebrow": "Smaller files, clear feedback",
        "heading": "Compress PDF.\nSee what changed.",
        "lead": "Reduce the size of scanned and image-heavy PDFs on your device, then see a clear before-and-after result when the new file is ready.",
        "image": "screen-tools",
        "image_alt": "Compress PDF option in the ProScan PDF tools page",
        "icon": "compress",
        "callout_title": "Before and after",
        "callout_text": "Original size, result and reduction.",
        "chips": ["Scanned PDFs", "Image PDFs", "Local processing", "Clear result"],
        "proofs": [
            ("compress", "Made for scanned documents", "The compressor rebuilds scanned and image-based pages with a more efficient image representation. That makes it useful for camera scans, photographed paperwork and PDFs created from photos."),
            ("document", "A separate compressed copy", "The original document is not silently overwritten. ProScan PDF creates a new compressed PDF so you can compare the result and keep the source when it matters."),
            ("check", "A result you can understand", "The completion card shows the original file size, the compressed file size and the percentage reduction instead of confirming the save without useful context."),
        ],
        "steps": [
            ("Choose a PDF", "Open Tools, tap Compress PDF and select the document from your library. Image-heavy scans are the best candidates because their pages contain the most compressible data."),
            ("Let the app rebuild the pages", "ProScan PDF renders and encodes the pages locally with settings intended to reduce storage size while keeping the document practical to read and share."),
            ("Review the reduction", "When processing finishes, the result card compares the original and compressed sizes and reports the percentage saved. The new PDF is available in My Files."),
        ],
        "details": [
            ("Useful before email and sharing", "A smaller PDF can be easier to attach to email, upload to a form or keep in a long-term document archive. Compression can also help when many scanned documents occupy local or iCloud storage."),
            ("Keeps orientation and page order", "The compressor rebuilds the PDF without intentionally changing the page sequence or mirroring the content. The finished document keeps the same reading direction and page order as the source."),
            ("Works inside the broader PDF workflow", "After compression, you can view, rename, organize, watermark, sign, lock or share the new copy. The result stays in the same library rather than being exported into a disconnected temporary location."),
        ],
        "note_title": "Where compression works best",
        "note": "Compression is optimized for scanned and image-based PDFs. A document made mostly from efficient vector text may already be compact, so its reduction can be modest. Re-rendering can also soften very fine image detail; keep the original when archival fidelity is essential.",
        "faqs": [
            ("Will compression overwrite my original PDF?", "No. ProScan PDF saves a separate compressed copy so the source remains available."),
            ("Which PDFs compress the most?", "Scanned pages, photos and other image-heavy PDFs usually produce the largest reductions."),
            ("Can I see how much space was saved?", "Yes. The success card displays the original size, compressed size and percentage reduction."),
            ("Does compression require an external server?", "No. The document is processed locally on your iPhone or iPad."),
        ],
        "related": ["add-watermark", "photo-to-pdf", "scan-to-pdf", "organize-pdf-pages"],
    },
    "sign-pdf": {
        "title": "Sign and Password-Protect PDFs on iPhone | ProScan PDF",
        "description": "Add signatures and text form boxes to PDFs, lock sensitive documents with a password and share the finished file from iPhone or iPad.",
        "eyebrow": "Finish documents securely",
        "heading": "Sign PDF.\nLock it before sending.",
        "lead": "Add a signature or text form item, protect sensitive PDFs with a password and share the finished document without leaving the app.",
        "image": "screen-sign",
        "image_alt": "Signature and text form options displayed over a PDF in ProScan PDF",
        "icon": "sign",
        "callout_title": "Sign and protect",
        "callout_text": "Finish paperwork from one place.",
        "chips": ["Signatures", "Text boxes", "Password lock", "Direct share"],
        "proofs": [
            ("sign", "Add a signature where it belongs", "Open a PDF, enter the form-editing flow and add a signature item to the page. The signature can be positioned as part of the document instead of being sent as a separate image."),
            ("document", "Complete simple form fields", "Add a text form box for names, dates, short answers and other information that needs to sit on top of the existing PDF page."),
            ("lock", "Protect sensitive files", "Create a password-protected PDF before sharing confidential paperwork. Locking is performed locally and produces an encrypted file for the recipient."),
        ],
        "steps": [
            ("Open the PDF you need to finish", "Choose the document from My Files and open the form-editing controls. The PDF remains visible while you decide whether to add text or a signature."),
            ("Place the form item", "Choose Add Text Form Box or Add Signature, then position the item on the appropriate page. Review the result before saving the modified PDF."),
            ("Lock or share the finished copy", "When the document is ready, use Lock to create a password-protected version or Share to send the file through the standard iOS share sheet."),
        ],
        "details": [
            ("A practical mobile signing flow", "The goal is to complete everyday paperwork without printing, signing and scanning it again. Signatures and text fields are integrated into the PDF workflow you already use for viewing and organizing pages."),
            ("Password protection is a separate decision", "Not every document needs encryption, so locking is available as an explicit action. You choose when a PDF should require a password rather than having security applied unexpectedly."),
            ("Clear completion feedback", "Saving a modified or signed PDF produces a confirmation card so you know the operation finished. Cache invalidation ensures the library and preview are refreshed after a file changes."),
        ],
        "note_title": "Share passwords separately",
        "note": "A password-protected PDF is only as secure as the password and the way it is communicated. Use a strong password and send it through a different channel from the protected document whenever the contents are sensitive.",
        "faqs": [
            ("Can I add both text and a signature?", "Yes. The form-item flow supports text form boxes and signatures on the PDF."),
            ("Can I lock a PDF with a password?", "Yes. The Lock action creates a password-protected PDF locally on the device."),
            ("How do I send the finished document?", "Use Share to open the standard iOS share sheet and choose an available destination."),
            ("Does signing upload the PDF to a server?", "No. The document editing and signing workflow is performed on your device."),
        ],
        "related": ["organize-pdf-pages", "scan-to-pdf", "pdf-to-word", "pdf-compressor"],
    },
    "pdf-to-word": {
        "title": "Convert PDF to Editable Word on iPhone | ProScan PDF",
        "description": "Convert PDF files to editable Word documents on iPhone or iPad. Layout-aware text positioning, local processing and honest limits for complex pages.",
        "eyebrow": "Editable text beyond the PDF",
        "heading": "PDF to Word.\nEdit the text again.",
        "lead": "Create a Word document with editable text and layout-aware positioning where possible, entirely on your iPhone or iPad.",
        "image": "screen-tools",
        "image_alt": "PDF to Word tool displayed in ProScan PDF",
        "icon": "word",
        "callout_title": "Editable Word output",
        "callout_text": "Preserve structure where possible.",
        "chips": ["Editable text", "Layout-aware", "DOCX output", "On-device"],
        "proofs": [
            ("word", "Text remains editable", "The conversion creates Word content rather than simply placing a full-page screenshot into the document. Recognized text can be selected and edited in a compatible word processor."),
            ("pages", "Position matters", "ProScan PDF uses detected text blocks and their page positions to approximate the source layout instead of sending every paragraph into one continuous left-aligned column."),
            ("lock", "Local document conversion", "OCR, text extraction and document generation happen on the device. The source PDF is not sent to a ProScan PDF conversion server."),
        ],
        "steps": [
            ("Choose the source PDF", "Open Tools, select PDF to Word and choose the document you want to convert. Clear text and straightforward page layouts provide the strongest starting point."),
            ("Recognize text and rebuild the page", "The app analyzes the PDF locally, identifies text regions and constructs an editable Word document while using the original page geometry to guide placement."),
            ("Open, share or continue editing", "The resulting Word file appears in My Files. Open it for a quick preview or share it to Microsoft Word, Pages or another compatible editor for further work."),
        ],
        "details": [
            ("Better than an image-only Word file", "A page image can preserve appearance perfectly but leaves the words locked inside a picture. ProScan PDF instead prioritizes editable text and adds layout information so the result remains useful after conversion."),
            ("Designed for common business documents", "Letters, forms, reports and documents with clear blocks of text are good candidates. The conversion is especially useful when the original editable file is unavailable and a section needs to be revised or reused."),
            ("One local workflow from scan to DOCX", "You can scan a paper document, save it as PDF, run OCR and create an editable Word version without uploading the paperwork to an external conversion website."),
        ],
        "note_title": "Complex layouts may need adjustment",
        "note": "No on-device converter can guarantee a pixel-perfect editable recreation of every PDF. Dense tables, unusual fonts, handwriting, overlapping elements and complex multi-column layouts may require manual cleanup. ProScan PDF preserves layout where possible rather than claiming perfect conversion.",
        "faqs": [
            ("Is the Word document editable?", "Yes. Recognized text is written as editable Word content rather than only as full-page images."),
            ("Will the layout look exactly the same?", "The app preserves detected positioning where possible, but complex pages can require manual adjustment in Word or Pages."),
            ("Where is the DOCX file saved?", "The generated Word document appears in My Files and can be opened or shared to another app."),
            ("Does conversion happen online?", "No. Text recognition and Word generation are performed locally on the device."),
        ],
        "related": ["ocr-text-extraction", "scan-to-pdf", "organize-pdf-pages", "sign-pdf"],
    },
    "id-photo-maker": {
        "title": "Passport and ID Photo Maker on iPhone | ProScan PDF",
        "description": "Create passport and ID photos in standard or custom sizes. Auto crop, quality checks, 300 DPI output and printable PDF sheets on iPhone or iPad.",
        "eyebrow": "Exact sizes from one photo",
        "heading": "ID Photo Maker.\nCrop with confidence.",
        "lead": "Take or import a portrait, crop it without distortion, review practical quality checks and export a single image or printable photo sheet.",
        "image": "screen-tools",
        "image_alt": "ID Photo Maker option on the ProScan PDF tools screen",
        "icon": "person",
        "callout_title": "Standard and custom sizes",
        "callout_text": "Single images or printable sheets.",
        "chips": ["Auto crop", "Quality checks", "300 DPI", "Printable sheets"],
        "proofs": [
            ("person", "Choose a practical photo size", "Use 35 × 45 mm, 40 × 50 mm, 50 × 50 mm, 50 × 60 mm, 50 × 70 mm, US 2 × 2 in or enter a custom width and height in millimeters or inches."),
            ("auto", "Crop without stretching", "Auto Crop uses face analysis to suggest framing while preserving the original image proportions. You can adjust the crop manually when the source or requirement needs a different composition."),
            ("check", "Review before export", "On-device checks assess face count and position, eye visibility when detectable, lighting, sharpness, background consistency and whether the crop supports a 300 DPI result."),
        ],
        "steps": [
            ("Take or choose a portrait", "Use the camera for a new photo or select an existing image. The source is prepared with the correct orientation so camera photos are not stretched or rotated incorrectly."),
            ("Choose size and refine the crop", "Select a standard format or enter a custom size, then use Auto Crop or manual pan and zoom controls. Quality guidance helps identify issues worth reviewing before export."),
            ("Export the format you need", "Create a JPEG or PNG single photo, or build a ready-to-print PDF sheet on A4, US Letter or 4 × 6 inch paper with repeated copies arranged at the selected physical size."),
        ],
        "details": [
            ("Physical dimensions, not guesswork", "The maker calculates output dimensions for print rather than treating an ID photo as an arbitrary square crop. Standard presets speed up common tasks, and the custom option covers requirements that use a different size."),
            ("Quality guidance remains on the device", "Face placement, pose, lighting, sharpness, background variation and resolution are analyzed locally. The checks are designed to help you notice common problems before printing without sending a portrait to an external service."),
            ("A printable sheet from one source", "Choose a paper size and ProScan PDF calculates how many photos fit with appropriate margins and spacing. The resulting PDF can be printed or shared, while JPEG and PNG remain available when a single digital photo is required."),
        ],
        "note_title": "Always check the official requirement",
        "note": "Photo rules vary by country, document type and issuing authority. ProScan PDF provides sizes, crop assistance and quality guidance, but it cannot guarantee acceptance. Confirm the current official dimensions, background, expression and printing rules before submitting an application.",
        "faqs": [
            ("Which sizes are included?", "The app includes 35 × 45, 40 × 50, 50 × 50, 50 × 60 and 50 × 70 mm, US 2 × 2 in and a custom-size option."),
            ("Can I make a printable sheet?", "Yes. Create a PDF sheet for A4, US Letter or 4 × 6 inch paper with repeated photos at the chosen physical size."),
            ("Does Auto Crop stretch the face?", "No. Cropping preserves the source proportions and selects a region that matches the target aspect ratio."),
            ("Does the tool guarantee government acceptance?", "No. Requirements vary, so you should always compare the result with the current rules from the issuing authority."),
        ],
        "related": ["photo-to-pdf", "scan-to-pdf", "pdf-compressor", "organize-pdf-pages"],
    },
    "ocr-text-extraction": {
        "title": "OCR Text Extraction and Searchable PDF on iPhone | ProScan PDF",
        "description": "Capture text with Live OCR, extract editable text from documents, create searchable PDFs and export to Word locally on iPhone or iPad.",
        "eyebrow": "Turn paper into useful text",
        "heading": "OCR text extraction.\nSearch what you scanned.",
        "lead": "Capture text live, recognize existing documents, create searchable PDF copies and move editable content into Word without sending the page to a server.",
        "image": "screen-ocr",
        "image_alt": "Live OCR recognizing text from a printed document in ProScan PDF",
        "icon": "search",
        "callout_title": "Live and document OCR",
        "callout_text": "Copy, search or export the text.",
        "chips": ["Live OCR", "Editable text", "Searchable PDF", "Word export"],
        "proofs": [
            ("eye", "Capture text through the camera", "Live OCR displays recognized text while the camera is aimed at a page. It is useful when you need the words quickly without first creating and opening a full PDF."),
            ("search", "Make a PDF searchable", "Search PDF creates a new searchable copy. Open that copy in the app’s PDF viewer and use its search control to find recognized words across the document."),
            ("word", "Reuse the text", "Extract document text for copying or generate an editable Word document with layout-aware positioning where the page structure allows it."),
        ],
        "steps": [
            ("Choose live capture or an existing file", "Use Live OCR from Home when the paper is in front of you, or choose Search PDF, PDF to Word or the OCR action for a document that is already in My Files."),
            ("Recognize text locally", "Apple Vision technology analyzes the page on your device. Clear print, good lighting, a straight page and sufficient image resolution improve recognition quality."),
            ("Use the result in the right form", "Copy editable text, save a text result, create a searchable PDF for in-app lookup or generate a Word file when the content needs further editing."),
        ],
        "details": [
            ("Searchable does not mean visually changed", "A searchable PDF keeps the familiar page appearance while adding recognized text information. That makes archived scans easier to find without replacing the original visual page with a plain text document."),
            ("Live OCR for quick capture", "Not every text task needs a PDF. Live OCR provides a faster route when you simply need to capture a paragraph, address, reference number or other printed content from the camera view."),
            ("A private OCR workflow", "Recognition is performed with on-device frameworks. ProScan PDF does not upload the scanned document to its own OCR server, which keeps sensitive notes, receipts and paperwork within your Apple device workflow."),
        ],
        "note_title": "Recognition depends on the source",
        "note": "OCR is strongest with sharp, well-lit printed text. Handwriting, decorative fonts, glare, folds, low contrast and complex tables can reduce accuracy. Review important names, numbers and legal text before relying on an extracted result.",
        "faqs": [
            ("How do I search a searchable PDF?", "Open the searchable copy in ProScan PDF’s viewer and use the search control to find recognized words."),
            ("Can I capture text without scanning a PDF first?", "Yes. Live OCR recognizes text directly from the camera view."),
            ("Can OCR create an editable Word file?", "Yes. PDF to Word uses recognized text and preserves layout where possible."),
            ("Is OCR processed on a server?", "No. The recognition workflow runs locally on your iPhone or iPad."),
        ],
        "related": ["pdf-to-word", "scan-to-pdf", "photo-to-pdf", "organize-pdf-pages"],
    },
    "organize-pdf-pages": {
        "title": "Extract, Reorder, Insert and Merge PDF Pages | ProScan PDF",
        "description": "Organize PDFs on iPhone or iPad: extract, reorder, insert or delete pages, merge files and save a clear modified copy locally.",
        "eyebrow": "Put every page in its place",
        "heading": "Organize PDF pages.\nKeep the useful parts.",
        "lead": "Extract, reorder, insert or delete pages, merge multiple PDFs and save a clear modified copy from the same document library.",
        "image": "screen-organize",
        "image_alt": "Six PDF page previews in the Organize Pages screen",
        "icon": "pages",
        "callout_title": "Page-level control",
        "callout_text": "Extract, reorder, insert and delete.",
        "chips": ["Extract pages", "Reorder", "Insert", "Merge PDFs"],
        "proofs": [
            ("pages", "See the document page by page", "Organize Pages presents visual previews so you can identify the page you need without guessing from a page number alone. Selected pages receive a clear highlighted state."),
            ("extract", "Create a focused PDF", "Select only the relevant pages and save them as a new extracted document. The original PDF stays available while the smaller result appears in My Files."),
            ("document", "Reshape an existing file", "Reorder pages, insert pages from another source or remove pages that should not remain. Save the modified PDF when the sequence is ready."),
        ],
        "steps": [
            ("Open Organize Pages", "Choose a PDF from My Files and tap Organize. Page previews appear in a dedicated workspace with Extract, Reorder, Insert and Delete actions."),
            ("Select the pages or operation", "Use selection for extraction or deletion, drag pages while reordering, or insert additional content. The interface keeps the operation visible so the result is easier to predict."),
            ("Save the right result", "Save extracted pages as a new PDF or save the modified document after reorder, insertion or deletion. A completion card confirms that the file was created successfully."),
        ],
        "details": [
            ("Extract without duplicating everything", "When only a few pages matter, extraction creates a concise PDF that is easier to share. It is useful for selected contract pages, one chapter, a receipt inside a larger scan or the relevant pages of a report."),
            ("Merge documents from My Files", "Selection mode supports combining multiple PDFs into one result. Choose the files, use Merge and save the new document without relying on an external upload-and-download service."),
            ("Immediate library feedback", "Deleted cards fade out and remaining files move into place with a controlled animation. Refreshes are coalesced so the library does not perform duplicate scans or replay the movement after one operation."),
        ],
        "note_title": "Keep originals for important documents",
        "note": "Page editing is designed to create clear modified or extracted results, but it is still good practice to keep an untouched original for legal, financial or archival documents until you have verified every page in the new file.",
        "faqs": [
            ("Can I extract only selected pages?", "Yes. Select the pages you need and save them as a new extracted PDF."),
            ("Can I change the page order?", "Yes. Choose Reorder, arrange the page previews and save the modified PDF."),
            ("Can I combine several PDFs?", "Yes. Use Select in My Files, choose the PDF files and tap Merge to create one combined document."),
            ("Does organizing require an upload?", "No. Extraction, reordering, insertion, deletion and merging are performed locally."),
        ],
        "related": ["sign-pdf", "add-watermark", "pdf-compressor", "scan-to-pdf"],
    },
}


ICONS = {
    "check": '<path d="m5 12.5 4.2 4.2L19 7"/>',
    "arrow-up-right": '<path d="M7 17 17 7M7 7h10v10"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "language": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "document": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v5h5M9.5 12h5M9.5 16h5"/>',
    "auto": '<path d="M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4"/><path d="m12 7 1.25 3.25L16.5 11.5l-3.25 1.25L12 16l-1.25-3.25L7.5 11.5l3.25-1.25z"/>',
    "pages": '<path d="M8 3h10v14H8z"/><path d="M5 7H3v14h10v-2M11 7h4M11 11h4"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v3"/>',
    "images": '<rect x="6" y="6" width="15" height="14" rx="2"/><path d="M3 16V5a2 2 0 0 1 2-2h12M8 17l4-4 3 3 2-2 2 2"/>',
    "photo": '<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="9" r="2"/><path d="m5.5 17 4.5-4 3 2.5 2.5-2 3 3.5"/>',
    "watermark": '<path d="M12 2s6 7 6 12a6 6 0 0 1-12 0c0-5 6-12 6-12Z"/><path d="M9 15c.7 1.7 2.4 2.4 4 1.8"/>',
    "compress": '<path d="M9 3v6H3M15 21v-6h6M4 8l5-5M20 16l-5 5"/>',
    "sign": '<path d="M4 18c3-5 5-7 6-6s-1 4 0 5 3-3 4-2-1 3 1 3c1.5 0 2.5-1 5-1"/><path d="m14 5 2-2 4 4-8 8-4 1 1-4z"/>',
    "word": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v5h5M9 12l1.2 5L12 13l1.8 4L15 12"/>',
    "person": '<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="12" cy="9" r="2.5"/><path d="M7.5 17c1-3 8-3 9 0"/>',
    "search": '<circle cx="10.5" cy="10.5" r="5.5"/><path d="m15 15 5 5"/><path d="M5 20h7"/>',
    "eye": '<path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"/><circle cx="12" cy="12" r="2.5"/>',
    "extract": '<path d="M7 3h8l4 4v14H7z"/><path d="M15 3v5h5M3 12h9M7 8l-4 4 4 4"/>',
    "cloud": '<path d="M7 19a5 5 0 0 1-.6-10A7 7 0 0 1 20 11.5 3.8 3.8 0 0 1 19 19Z"/><path d="m9 14 3-3 3 3M12 11v7"/>',
}


LANGUAGE_LINKS = [
    ("/", "en", "English"), ("/de/", "de", "Deutsch"), ("/fr/", "fr", "Français"),
    ("/es/", "es", "Español"), ("/it/", "it", "Italiano"), ("/nl/", "nl", "Nederlands"),
    ("/pt-br/", "pt-BR", "Português (Brasil)"), ("/pt-pt/", "pt-PT", "Português (Portugal)"),
    ("/pl/", "pl", "Polski"), ("/tr/", "tr", "Türkçe"), ("/zh-hans/", "zh-Hans", "简体中文"),
    ("/ja/", "ja", "日本語"), ("/ko/", "ko", "한국어"), ("/hi/", "hi", "हिन्दी"),
]


def svg_sprite() -> str:
    return "\n".join(
        f'        <symbol id="icon-{name}" viewBox="0 0 24 24">{paths}</symbol>'
        for name, paths in ICONS.items()
    )


def icon(name: str) -> str:
    return f'<svg aria-hidden="true"><use href="#icon-{name}"></use></svg>'


def json_ld(slug: str, item: dict) -> str:
    canonical = f"https://proscanpdf.com/{slug}/"
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{canonical}#webpage",
                "url": canonical,
                "name": item["title"],
                "description": item["description"],
                "inLanguage": "en",
                "isPartOf": {"@id": "https://proscanpdf.com/#website"},
                "about": {"@id": "https://proscanpdf.com/#app"},
                "dateModified": "2026-08-22",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://proscanpdf.com/"},
                    {"@type": "ListItem", "position": 2, "name": item["heading"].replace("\n", " "), "item": canonical},
                ],
            },
            {
                "@type": "HowTo",
                "name": item["heading"].replace("\n", " "),
                "description": item["lead"],
                "step": [
                    {"@type": "HowToStep", "position": index, "name": title, "text": text}
                    for index, (title, text) in enumerate(item["steps"], 1)
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
                    for question, answer in item["faqs"]
                ],
            },
            {
                "@type": "MobileApplication",
                "@id": "https://proscanpdf.com/#app",
                "name": "ProScan PDF",
                "url": "https://proscanpdf.com/",
                "downloadUrl": APP_STORE,
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "iOS, iPadOS",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            {
                "@type": "Organization",
                "@id": "https://proscanpdf.com/#organization",
                "name": "ProScan PDF",
                "url": "https://proscanpdf.com/",
                "logo": {"@type": "ImageObject", "url": "https://proscanpdf.com/appicon.png"},
                "sameAs": [APP_STORE, "https://paulcrp.com/"],
            },
            {
                "@type": "WebSite",
                "@id": "https://proscanpdf.com/#website",
                "url": "https://proscanpdf.com/",
                "name": "ProScan PDF",
                "publisher": {"@id": "https://proscanpdf.com/#organization"},
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=6)


def render_page(slug: str, item: dict) -> str:
    heading_parts = [html.escape(part) for part in item["heading"].split("\n")]
    heading = heading_parts[0] if len(heading_parts) == 1 else f'{heading_parts[0]}<br><span>{" ".join(heading_parts[1:])}</span>'
    canonical = f"https://proscanpdf.com/{slug}/"
    language_options = "\n".join(
        f'                        <a href="{path}" lang="{lang}" hreflang="{lang}"{(" aria-current=\"page\"" if lang == "en" else "")}>{label}</a>'
        for path, lang, label in LANGUAGE_LINKS
    )
    chips = "".join(f'<span>{icon("check")}{html.escape(label)}</span>' for label in item["chips"])
    proofs = "\n".join(
        f'''                <article class="guide-proof reveal">
                    <div class="guide-icon">{icon(symbol)}</div>
                    <h2>{html.escape(title)}</h2>
                    <p>{html.escape(text)}</p>
                </article>'''
        for symbol, title, text in item["proofs"]
    )
    steps = "\n".join(
        f'''                <article class="guide-step reveal">
                    <span class="guide-step-number">{index:02d}</span>
                    <h3>{html.escape(title)}</h3>
                    <p>{html.escape(text)}</p>
                </article>'''
        for index, (title, text) in enumerate(item["steps"], 1)
    )
    details = "\n".join(
        f'''                <article class="guide-detail reveal">
                    <h2>{html.escape(title)}</h2>
                    <p>{html.escape(text)}</p>
                </article>'''
        for title, text in item["details"]
    )
    faqs = "\n".join(
        f'<details><summary>{html.escape(question)}<span aria-hidden="true"></span></summary><p>{html.escape(answer)}</p></details>'
        for question, answer in item["faqs"]
    )
    related = "\n".join(
        f'''                <a class="related-guide reveal" href="/{related_slug}/">
                    <div class="guide-icon">{icon(FEATURES[related_slug]["icon"])}</div>
                    <h3>{html.escape(FEATURES[related_slug]["heading"].replace(chr(10), " "))}</h3>
                    <p>{html.escape(FEATURES[related_slug]["lead"])}</p>
                </a>'''
        for related_slug in item["related"]
    )
    return f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{html.escape(item["title"])}</title>
    <meta name="description" content="{html.escape(item["description"], quote=True)}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="theme-color" content="#12171B">
    <meta name="apple-itunes-app" content="app-id=6752308731">
    <link rel="canonical" href="{canonical}">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon-paper-on-ink.svg?v=paper-1">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=paper-1">
    <link rel="shortcut icon" href="/favicon.ico?v=paper-1">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=paper-1">
    <link rel="preload" href="../assets/fonts/nunito-latin.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" as="image" href="../assets/{item["image"]}.webp" imagesrcset="../assets/{item["image"]}-360.webp 360w, ../assets/{item["image"]}-540.webp 540w, ../assets/{item["image"]}.webp 720w" imagesizes="(max-width: 700px) 70vw, 350px" type="image/webp">
    <link rel="stylesheet" href="../styles.min.css?v=seo-guides-4">

    <meta property="og:type" content="website">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="ProScan PDF">
    <meta property="og:title" content="{html.escape(item["title"], quote=True)}">
    <meta property="og:description" content="{html.escape(item["description"], quote=True)}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="https://proscanpdf.com/assets/proscan-social-card.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="ProScan PDF scanner and PDF tools">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(item["title"], quote=True)}">
    <meta name="twitter:description" content="{html.escape(item["description"], quote=True)}">
    <meta name="twitter:image" content="https://proscanpdf.com/assets/proscan-social-card.webp">

    <script type="application/ld+json">
{json_ld(slug, item)}
    </script>
</head>
<body class="feature-page">
    <a class="skip-link" href="#main-content">Skip to content</a>
    <svg class="svg-sprite" aria-hidden="true">
{svg_sprite()}
    </svg>

    <header class="site-header" data-header>
        <nav class="nav-shell" aria-label="Main navigation">
            <a class="brand" href="/" aria-label="ProScan PDF home">
                <span class="brand-icon"><img src="../assets/proscan-mark.svg" alt="" width="40" height="40"></span>
                <span>ProScan PDF</span>
            </a>
            <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" data-nav-toggle>
                <span></span><span></span><span></span><span class="sr-only">Open navigation</span>
            </button>
            <div class="nav-menu" id="nav-menu" data-nav-menu>
                <a href="/#scanner">Scanner</a><a href="/#tools">PDF Tools</a><a href="/#privacy">Privacy</a><a href="#faq">FAQ</a>
            </div>
            <div class="header-actions">
                <details class="language-selector" data-language-selector>
                    <summary aria-label="EN — Choose language">{icon("language")}<span>EN</span><svg class="language-chevron" aria-hidden="true"><use href="#icon-chevron-down"></use></svg></summary>
                    <div class="language-options" aria-label="Language">
{language_options}
                    </div>
                </details>
                <a class="nav-cta" href="{APP_STORE}" data-app-store="navigation" rel="noopener">Get the app</a>
            </div>
        </nav>
    </header>

    <main id="main-content">
        <section class="feature-hero" id="top">
            <div class="hero-noise" aria-hidden="true"></div>
            <div class="feature-hero-grid section-shell">
                <div class="feature-copy">
                    <nav class="feature-breadcrumbs" aria-label="Breadcrumb"><a href="/">ProScan PDF</a><span aria-hidden="true">/</span><span>{html.escape(item["heading"].split(chr(10))[0])}</span></nav>
                    <p class="eyebrow hero-enter">{html.escape(item["eyebrow"])}</p>
                    <h1 class="hero-enter">{heading}</h1>
                    <p class="hero-lead hero-enter">{html.escape(item["lead"])}</p>
                    <div class="feature-chip-row hero-enter">{chips}</div>
                    <a class="official-store-link hero-enter" href="{APP_STORE}" data-app-store="feature-hero" rel="noopener" aria-label="Download ProScan PDF on the App Store"><img src="../assets/download-on-app-store-en.svg" width="210" height="70" alt="Download on the App Store"></a>
                </div>
                <div class="feature-visual hero-enter" aria-label="{html.escape(item["image_alt"], quote=True)}">
                    <div class="device feature-device"><div class="device-sensor" aria-hidden="true"></div><img src="../assets/{item["image"]}.webp" srcset="../assets/{item["image"]}-360.webp 360w, ../assets/{item["image"]}-540.webp 540w, ../assets/{item["image"]}.webp 720w" sizes="(max-width: 700px) 70vw, 350px" width="720" height="1566" alt="{html.escape(item["image_alt"], quote=True)}" fetchpriority="high"></div>
                    <div class="feature-callout"><span>{icon(item["icon"])}</span><div><strong>{html.escape(item["callout_title"])}</strong><small>{html.escape(item["callout_text"])}</small></div></div>
                </div>
            </div>
        </section>

        <section class="guide-intro section-shell" aria-label="Key benefits"><div class="guide-proof-grid">{proofs}</div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">A clear three-step workflow</p><h2>From source to<br><span>finished result.</span></h2><p>ProScan PDF keeps the action, confirmation and saved file inside one focused workflow.</p></div>
            <div class="guide-step-grid">{steps}</div>
        </div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">Built for practical documents</p><h2>Useful details.<br><span>Honest expectations.</span></h2></div>
            <div class="guide-detail-grid">{details}</div>
            <aside class="honest-note reveal">{icon("check")}<div><h2>{html.escape(item["note_title"])}</h2><p>{html.escape(item["note"])}</p></div></aside>
        </div></section>

        <section class="faq-section feature-faq guide-section" id="faq"><div class="section-shell faq-grid">
            <div class="faq-intro reveal"><p class="eyebrow">Questions, answered</p><h2>Before you<br><span>begin.</span></h2><p>Practical details about how this feature works in ProScan PDF.</p></div>
            <div class="faq-list reveal">{faqs}</div>
        </div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">Continue the workflow</p><h2>More ways to<br><span>finish the document.</span></h2></div>
            <div class="related-guide-grid">{related}</div>
        </div></section>

        <section class="download-section section-pad"><div class="section-shell download-card reveal">
            <div class="download-mark"><img src="../assets/proscan-mark.svg" alt="" width="104" height="104"></div>
            <p class="eyebrow">Your next document is one tap away</p><h2>Scan clean.<br><span>Work privately.</span></h2><p>No ads. No watermarks.</p>
            <a class="official-store-link" href="{APP_STORE}" data-app-store="final-cta" rel="noopener" aria-label="Download ProScan PDF on the App Store"><img src="../assets/download-on-app-store-en.svg" width="210" height="70" alt="Download on the App Store"></a>
        </div></section>
    </main>

    <footer class="site-footer"><div class="section-shell footer-grid">
        <div class="footer-brand"><a class="brand" href="/"><span class="brand-icon"><img src="../assets/proscan-mark.svg" alt="" width="40" height="40"></span><span>ProScan PDF</span></a><p>A private document scanner and complete PDF toolkit for iPhone and iPad.</p></div>
        <div class="footer-links">
            <div><strong>Product</strong><a href="/scan-to-pdf/">Scan to PDF</a><a href="/photo-to-pdf/">Photos to PDF</a><a href="/ocr-text-extraction/">OCR</a><a href="/organize-pdf-pages/">Organize PDFs</a></div>
            <div><strong>PDF Tools</strong><a href="/pdf-to-images/">PDF to Images</a><a href="/add-watermark/">Add Watermark</a><a href="/pdf-compressor/">Compress PDF</a><a href="/pdf-to-word/">PDF to Word</a><a href="/sign-pdf/">Sign and lock</a><a href="/id-photo-maker/">ID Photo Maker</a></div>
            <div><strong>More</strong><a href="{APP_STORE}" data-app-store="footer" rel="noopener">App Store</a><a href="https://paulcrp.com/proscanpdf_privacypolicy.html" rel="noopener">Privacy Policy</a><a href="mailto:info@proscanpdf.com">Contact support</a></div>
        </div>
    </div><div class="section-shell footer-bottom"><span>© <span data-year></span> ProScan PDF</span><span>Made for focused work.</span></div></footer>
    <script src="../script.min.js?v=seo-guides-2" defer></script>
</body>
</html>
'''


def main() -> None:
    for slug, item in FEATURES.items():
        target = ROOT / slug
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(render_page(slug, item), encoding="utf-8")
    print(f"Generated {len(FEATURES)} feature guides")


if __name__ == "__main__":
    main()
