# Skyline Soaring Club Member Portal - Roadmap

This roadmap outlines current and future development goals for the Skyline Soaring Club Member Portal. Items marked as ✅ are complete.

## Completed Tasks ✅
- Move Django SECRET_KEY to `.env` file and rotate it.
- Replace `@login_required` with `@active_member_required` for superuser access.
- Set up Google OAuth2 login, including:
   - Safe credential storage in `.env`
   - First login with Google OAuth creates an account with default status
   - First login with username/password then allows later OAuth2 login (email match)
   - OAuth2 login can import Google profile photo
- Enforce profile photo uploads to be resized and aspect-ratio checked.
- Add support for rich biography field with TinyMCE and image upload.
- Enable users to upload profile photos; allow self-service photo edits.
- Add vCard QR code to member_view.html with proper home contact tagging.
- Add badge management system:
   - Admin-editable badges with HTML descriptions
   - Member-badge relationship with award date
   - Badge board with thumbnails of recipients
   - Accordion-style badge descriptions
   - Ordered badge display
- Add member name formatting helper (`get_display_name`)
- Improve navigation UI and add responsive hamburger menu.
- Setup flatpickr calendar popup for ISO 8601 date input.
- Automated profile photos using Pydenticon instead of the static image. 
- States should be a pull-down.  (Complicated by the fact that we have non-US ex members)
- Hyphenate phone numbers so the phone numbers don't look like barbaric strings of digits
- members_list page: differentiate home vs cell phone numbers. 
- members_list page: sort by lastname in a default view.  
- Create restricted site for Instructors

---

## On Hold tasks 🛑
- Migration tooling for importing legacy member data from PostgreSQL JSON export
- create flight log tables in preparation for logsheet program. 

---

## In Progress 🔄
- Improve member import with robust date parsing and dry-run validation

---

## Abandoned Tasks ⚰️
1. Allow uploading vCard files to populate members (**deprioritized**)


---

## Upcoming Tasks 🚀
- Add support for importing badge achievements from legacy system
- Set up OAuth2 login for providers other than Google (Yahoo, Microsoft, Facebook)
- Admin UI for editing badge recipients in a non-admin interface
- Integrate legacy usernames (handle) to link historical flight log data
- Customize Django admin list display to show additional fields like `membership_status`, `towpilot`, `glider_rating`, etc.
- Allow members to view but not edit their own membership records (except photo & biography)
- Add glider image thumbnails to members who own gliders
- Add contact group management (for targeted emails)
- Add flight history viewer (imported legacy data + new log uploads)
- Import Training Syllabus

---

## Nice-to-Haves / Stretch Goals
- Add calendar of events (duty roster, instructor availability, club events)
- Member activity timeline (badge earned, glider flights, etc.)
- CSV, XLS or PDF export of member list for club use
- Automatic backup and restore scripts for database/media
- Dockerize deployment

---

If you have questions, suggestions, or contributions, please open an issue or reach out to Piet Barber!

## Logsheet Program – Future Enhancements

- [ ] Support logging of passengers:
  - Passenger may be a member (dropdown) or a non-member (plain text).
  - Field is only visible if no instructor is present on the flight.

- [ ] Implement logsheet-level finances:
  - Add a Finances modal or section, accessible via a dedicated button.
  - Completion of finances is required before finalizing a logsheet.

- [ ] Define tow altitude rate model:
  - Create a model under `logsheet` to store tow altitude → cost mappings.
  - Combine with existing glider rental rates.

- [ ] Add support for payment methods:
  - "On account" or handwritten check.
  - Payments may be assigned to a member other than the pilot.
  - Support 50/50 cost splits or split by component (tow vs rental).

- [ ] Require duty officer log/essay before logsheet finalization.

- [ ] Block finalization unless all gliders are marked as landed.

- [ ] Centralized validation logic before allowing logsheet finalization:
  - Gliders landed
  - Finances completed
  - Duty officer essay entered

- [ ] Migration tool for legacy flight logs:
  - Import historical PostgreSQL data going back to 2005.
  - Must integrate with current Member, Glider, and Towplane models.

- [ ] Paginated or limited logsheet list:
  - Display most recent year or 50 logsheets by default.
  - Include search or filter capability for older logsheets.

- [ ] Offline-compatible logsheet entry:
  - Support local Django instance with full flight logging functionality.
  - End-of-day synchronization to live server (e.g., push finalized logsheets).

- [ ] Export finalized logsheets to CSV for Quickbooks Online:
  - Output must meet QBO format requirements.
  - May include member name, aircraft, cost breakdown, and payment method.