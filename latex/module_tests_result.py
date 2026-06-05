Found 19 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: channels, corsheaders, daphne, django_filters, drf_spectacular, messages, rest_framework, staticfiles
  Apply all migrations: admin, auth, bookings, chats, contenttypes, contracts, items, notifications, postoffices, sessions, users
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying items.0001_initial... OK
  Applying items.0002_category_item_category... OK
  Applying items.0003_itemimage... OK
  Applying bookings.0001_initial... OK
  Applying bookings.0002_review... OK
  Applying bookings.0003_booking_paid_at_booking_payment_expires_at_and_more... OK
  Applying bookings.0004_review_is_hidden_review_moderated_at_and_more... OK
  Applying bookings.0005_booking_pickup_point... OK
  Applying bookings.0006_booking_deposit_amount_booking_deposit_expires_at_and_more... OK
  Applying bookings.0007_booking_owner_return_confirmed_and_more... OK
  Applying bookings.0008_booking_platform_fee_booking_rent_amount... OK
  Applying items.0004_item_average_rating_item_reviews_count... OK
  Applying items.0005_itemvideo... OK
  Applying items.0006_alter_itemimage_options_alter_itemvideo_options... OK
  Applying chats.0001_initial... OK
  Applying chats.0002_chat_item... OK
  Applying contracts.0001_initial... OK
  Applying items.0007_itemreview... OK
  Applying items.0008_rename_items_itemr_item_id_3f6d3c_idx_items_itemr_item_id_fe3bc0_idx_and_more... OK
  Applying items.0009_item_moderation... OK
  Applying items.0010_russian_moderation_choice_labels... OK
  Applying items.0011_item_deposit... OK
  Applying notifications.0001_initial... OK
  Applying notifications.0002_alter_notification_type... OK
  Applying notifications.0003_notification_metadata_alter_notification_type... OK
  Applying notifications.0004_alter_notification_type... OK
  Applying postoffices.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying users.0002_remove_user_role_user_profile_completed_and_more... OK
  Applying users.0003_user_average_rating_user_reviews_count... OK
  Applying users.0004_user_inn_user_kpp_user_ogrnip_user_passport_number... OK
  Applying users.0005_user_passport_series_alter_user_passport_number... OK
  Applying users.0006_alter_user_email... OK
  Applying users.0007_user_company_name_user_entrepreneur_name_and_more... OK
System check identified no issues (0 silenced).
test_chat_members (chats.tests.ChatTest.test_chat_members) ... ok
test_conversations_are_sorted_by_last_message (chats.tests.ChatTest.test_conversations_are_sorted_by_last_message) ... ok
test_create_conversation_is_separated_by_item (chats.tests.ChatTest.test_create_conversation_is_separated_by_item) ... ok
test_create_empty_message_via_api_is_rejected (chats.tests.ChatTest.test_create_empty_message_via_api_is_rejected) ... ok
test_create_message (chats.tests.ChatTest.test_create_message) ... ok
test_create_message_with_image_via_api (chats.tests.ChatTest.test_create_message_with_image_via_api) ... ok
test_mark_read_returns_updated_message_ids (chats.tests.ChatTest.test_mark_read_returns_updated_message_ids) ... ok
test_support_faq_is_available_without_auth (chats.tests.ChatTest.test_support_faq_is_available_without_auth) ... ok
test_booking_creation_creates_owner_notification (notifications.tests.NotificationTests.test_booking_creation_creates_owner_notification) ... ok
test_confirm_booking_creates_renter_notification (notifications.tests.NotificationTests.test_confirm_booking_creates_renter_notification) ... ok
test_legacy_return_reminder_command_creates_correct_notification (notifications.tests.NotificationTests.test_legacy_return_reminder_command_creates_correct_notification) ... Отправлено 1 напоминаний о возврате
ok
test_mark_notification_read_endpoints (notifications.tests.NotificationTests.test_mark_notification_read_endpoints) ... ok
test_new_message_notification_contains_chat_metadata (notifications.tests.NotificationTests.test_new_message_notification_contains_chat_metadata) ... ok
test_payment_confirmed_notification_points_to_my_items (notifications.tests.NotificationTests.test_payment_confirmed_notification_points_to_my_items) ... ok
test_payment_confirmed_sends_email (notifications.tests.NotificationTests.test_payment_confirmed_sends_email) ... ok
test_return_reminder_creates_notification (notifications.tests.NotificationTests.test_return_reminder_creates_notification) ... ok
test_contract_is_unavailable_for_pending_booking (contracts.tests.ContractApiTest.test_contract_is_unavailable_for_pending_booking) ... ok
test_participant_can_open_contract_by_booking (contracts.tests.ContractApiTest.test_participant_can_open_contract_by_booking) ... ok
test_renter_and_owner_can_sign_contract_with_demo_eds (contracts.tests.ContractApiTest.test_renter_and_owner_can_sign_contract_with_demo_eds) ... ok

----------------------------------------------------------------------
Ran 19 tests in 36.344s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...