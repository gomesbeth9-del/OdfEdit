import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import OdfEdit_linux

def test_import_module():
    assert hasattr(OdfEdit_linux, 'C_LOGS')
    assert hasattr(OdfEdit_linux, 'C_AUDIO_PLAYER')
    assert hasattr(OdfEdit_linux, 'C_ODF_MISC')
    assert hasattr(OdfEdit_linux, 'C_ODF_DATA_CHECK')

def test_C_LOGS_add_and_get():
    logs = OdfEdit_linux.C_LOGS()
    logs.clear()
    logs.add('test log')
    assert 'test log' in logs.get()

def test_C_LOGS_nb_get():
    logs = OdfEdit_linux.C_LOGS()
    logs.clear()
    logs.add('log1')
    logs.add('log2')
    assert logs.nb_get() == 2

def test_C_LOGS_clear():
    logs = OdfEdit_linux.C_LOGS()
    logs.add('log')
    logs.clear()
    assert logs.nb_get() == 0

def test_C_AUDIO_PLAYER_init():
    player = OdfEdit_linux.C_AUDIO_PLAYER()
    assert hasattr(player, 'playback_in_progress')

def test_C_AUDIO_PLAYER_pause_resume():
    player = OdfEdit_linux.C_AUDIO_PLAYER()
    player.playback_in_progress = True
    player.playback_paused = False
    player.pause_resume()
    assert player.playback_paused is True
    player.pause_resume()
    assert player.playback_paused is False

def test_C_AUDIO_PLAYER_stop():
    player = OdfEdit_linux.C_AUDIO_PLAYER()
    player.playback_in_progress = True
    player.stream = None
    player.stop()
    assert player.playback_in_progress is False

def test_C_ODF_MISC_init():
    misc = OdfEdit_linux.C_ODF_MISC()
    assert hasattr(misc, 'compass_get')

def test_C_ODF_DATA_CHECK_init():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_odf_data')

def test_constants_exist():
    assert hasattr(OdfEdit_linux, 'APP_VERSION')
    assert hasattr(OdfEdit_linux, 'RELEASE_DATE')
    assert hasattr(OdfEdit_linux, 'MAIN_WINDOW_TITLE')

def test_allowed_chars():
    chars = OdfEdit_linux.ALLOWED_CHARS_4_FIELDS
    assert '_' in chars
    assert 'A' in chars
    assert 'z' in chars

def test_notes_names():
    assert 'C' in OdfEdit_linux.NOTES_NAMES
    assert 'Cis' in OdfEdit_linux.NOTES_NAMES2

def test_compass_extend_manual_exists():
    misc = OdfEdit_linux.C_ODF_MISC()
    assert hasattr(misc, 'compass_extend_manual')

def test_compass_extend_stop_exists():
    misc = OdfEdit_linux.C_ODF_MISC()
    assert hasattr(misc, 'compass_extend_stop')

def test_compass_extend_rank_exists():
    misc = OdfEdit_linux.C_ODF_MISC()
    assert hasattr(misc, 'compass_extend_rank')

def test_check_panel_format_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_panel_format')

def test_check_object_uid_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_uid')

def test_check_object_line_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_line')

def test_check_object_Header_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Header')

def test_check_object_Organ_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Organ')

def test_check_object_Coupler_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Coupler')

def test_check_object_Divisional_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Divisional')

def test_check_object_DivisionalCoupler_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_DivisionalCoupler')

def test_check_object_DrawStop_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_DrawStop')

def test_check_object_Button_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Button')

def test_check_object_PushButton_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_PushButton')

def test_check_object_Manual_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Manual')

def test_check_object_Panel_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Panel')

def test_check_object_PanelElement_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_PanelElement')

def test_check_object_Rank_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Rank')

def test_check_object_Stop_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Stop')

def test_check_object_Switch_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Switch')

def test_check_object_Tremulant_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_Tremulant')

def test_check_object_WindchestGroup_exists():
    check = OdfEdit_linux.C_ODF_DATA_CHECK()
    assert hasattr(check, 'check_object_WindchestGroup')

    # Additional 10 tests for broader coverage
    def test_COMPASS_EXTEND_MAX_value():
        assert isinstance(OdfEdit_linux.COMPASS_EXTEND_MAX, int)
        assert OdfEdit_linux.COMPASS_EXTEND_MAX > 0

    def test_COLOR_BACKGROUND0_format():
        color = OdfEdit_linux.COLOR_BACKGROUND0
        assert isinstance(color, str)
        assert color.startswith('#')
        assert len(color) == 7

    def test_TAGS_and_COLORS_exist():
        assert hasattr(OdfEdit_linux, 'TAG_OBJ_UID')
        assert hasattr(OdfEdit_linux, 'COLOR_TAG_OBJ_UID')

    def test_C_LOGS_multiple_instances():
        logs1 = OdfEdit_linux.C_LOGS()
        logs2 = OdfEdit_linux.C_LOGS()
        logs1.clear()
        logs2.clear()
        logs1.add('a')
        logs2.add('b')
        assert 'a' in logs1.get()
        assert 'b' in logs2.get()

    def test_C_AUDIO_PLAYER_wav_data_get_missing_file():
        player = OdfEdit_linux.C_AUDIO_PLAYER()
        result = player.wav_data_get('nonexistent_file.wav')
        assert 'error_msg' in result
        assert result['error_msg'] != ''

    def test_C_ODF_MISC_compass_get_returns_none():
        misc = OdfEdit_linux.C_ODF_MISC()
        # Should return None for unknown object_uid
        assert misc.compass_get('UnknownObject') is None

    def test_C_ODF_DATA_CHECK_check_object_uid_invalid():
        check = OdfEdit_linux.C_ODF_DATA_CHECK()
        # Should return error for invalid UID
        assert check.check_object_uid('Invalid!UID') is not None

    def test_C_ODF_DATA_CHECK_check_object_line_bracket():
        check = OdfEdit_linux.C_ODF_DATA_CHECK()
        # Should detect missing closing bracket
        error, attr, val, comment = check.check_object_line('[UID', True)
        assert error is not None

    def test_C_ODF_DATA_CHECK_check_object_line_equal():
        check = OdfEdit_linux.C_ODF_DATA_CHECK()
        # Should detect line starting with '='
        error, attr, val, comment = check.check_object_line('=value', True)
        assert error is not None

    def test_C_ODF_DATA_CHECK_check_object_line_comment():
        check = OdfEdit_linux.C_ODF_DATA_CHECK()
        # Should treat ';comment' as a comment
        error, attr, val, comment = check.check_object_line(';this is a comment', True)
        assert error is None
        assert comment is not None
