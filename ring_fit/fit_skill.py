from enum import Enum


class FitSkillType(Enum):
    ARMS = 'うで'
    ABS = 'はら'
    LEGS = 'あし'
    YOGA = 'ヨガ'


class FitSkill:
    name: str
    type: FitSkillType


class BackPress(FitSkill):
    name = 'ウシロプッシュ'
    type = FitSkillType.ARMS


class OverheadPress(FitSkill):
    name = 'バンザイプッシュ'
    type = FitSkillType.ARMS


class FrontPress(FitSkill):
    name = 'サゲテプッシュ'
    type = FitSkillType.ARMS


class BowPull(FitSkill):
    name = 'リングアロー'
    type = FitSkillType.ARMS


class ShoulderPress(FitSkill):
    name = 'カタニプッシュ'
    type = FitSkillType.ARMS


class TricepKickback(FitSkill):
    name = 'トライセプス'
    type = FitSkillType.ARMS


class OverheadArmTwist(FitSkill):
    name = 'アームツイスト'
    type = FitSkillType.ARMS


class OverheadArmSpin(FitSkill):
    name = 'グルグルアーム'
    type = FitSkillType.ARMS


class OverheadSideBend(FitSkill):
    name = 'バンザイサイドベンド'
    type = FitSkillType.ABS


class OverheadLungeTwist(FitSkill):
    name = 'バンザイツイスト'
    type = FitSkillType.ABS


class PendulumBend(FitSkill):
    name = 'ベントオーバー'
    type = FitSkillType.ABS


class OverheadBend(FitSkill):
    name = 'バンザイモーニング'
    type = FitSkillType.ABS


class KneeToChest(FitSkill):
    name = 'ニートゥーチェスト'
    type = FitSkillType.ABS


class SeatedForwardPress(FitSkill):
    name = 'マエニプッシュ'
    type = FitSkillType.ABS


class Plank(FitSkill):
    name = 'プランク'
    type = FitSkillType.ABS


class LegRaise(FitSkill):
    name = 'レッグレイズ'
    type = FitSkillType.ABS


class OpenCloseLegRaise(FitSkill):
    name = 'アシパカパカ'
    type = FitSkillType.ABS


class StandingTwist(FitSkill):
    name = 'スワイショウ'
    type = FitSkillType.ABS


class OverheadHipShake(FitSkill):
    name = 'バンザイコシフリ'
    type = FitSkillType.ABS


class RussianTwist(FitSkill):
    name = 'ロシアンツイスト'
    type = FitSkillType.ABS


class FlutterKick(FitSkill):
    name = 'バタバタレッグ'
    type = FitSkillType.ABS


class SeatedRingRaise(FitSkill):
    name = 'リングアゲサゲ'
    type = FitSkillType.ABS


class LegScissors(FitSkill):
    name = 'リングアゲサゲ'
    type = FitSkillType.ABS


class Squat(FitSkill):
    name = 'スクワット'
    type = FitSkillType.LEGS


class WideSquat(FitSkill):
    name = 'ワイドスクワット'
    type = FitSkillType.LEGS


class OverheadSquat(FitSkill):
    name = 'バンザイスクワット'
    type = FitSkillType.LEGS


class ThighPress(FitSkill):
    name = 'モモデプッシュ'
    type = FitSkillType.LEGS


class HipLift(FitSkill):
    name = 'ヒップリフト'
    type = FitSkillType.LEGS


class MountainClimber(FitSkill):
    name = 'マウンテンクライマー'
    type = FitSkillType.LEGS


class KneeLift(FitSkill):
    name = 'モモアゲアゲ'
    type = FitSkillType.LEGS


class SideStep(FitSkill):
    name = 'ステップアップ'
    type = FitSkillType.LEGS


class RingRaiseCombo(FitSkill):
    name = 'アゲサゲコンボ'
    type = FitSkillType.LEGS


class KneeLiftCombo(FitSkill):
    name = 'モモアゲコンボ'
    type = FitSkillType.LEGS


class ChairPose(FitSkill):
    name = '椅子のポーズ'
    type = FitSkillType.YOGA


class TreePose(FitSkill):
    name = '立木のポーズ'
    type = FitSkillType.YOGA


class HingePose(FitSkill):
    name = 'チョウツガイのポーズ'
    type = FitSkillType.YOGA


class RevolvedCrescentLungePose(FitSkill):
    name = 'ねじり体側のポーズ'
    type = FitSkillType.YOGA


class Warrior1Pose(FitSkill):
    name = '英雄1のポーズ'
    type = FitSkillType.YOGA


class Warrior2Pose(FitSkill):
    name = '英雄2のポーズ'
    type = FitSkillType.YOGA


class Warrior3Pose(FitSkill):
    name = '英雄3のポーズ'
    type = FitSkillType.YOGA


class FanPose(FitSkill):
    name = '扇のポーズ'
    type = FitSkillType.YOGA


class BoatPose(FitSkill):
    name = '舟のポーズ'
    type = FitSkillType.YOGA


class StandingForwardFold(FitSkill):
    name = '折りたたむポーズ'
    type = FitSkillType.YOGA


FIT_SKILLS = {
    BackPress,
    OverheadPress,
    FrontPress,
    BowPull,
    ShoulderPress,
    TricepKickback,
    OverheadArmTwist,
    OverheadArmSpin,
    OverheadSideBend,
    OverheadLungeTwist,
    PendulumBend,
    OverheadBend,
    KneeToChest,
    SeatedForwardPress,
    Plank,
    LegRaise,
    OpenCloseLegRaise,
    StandingTwist,
    OverheadHipShake,
    RussianTwist,
    FlutterKick,
    SeatedRingRaise,
    LegScissors,
    Squat,
    WideSquat,
    OverheadSquat,
    ThighPress,
    HipLift,
    MountainClimber,
    KneeLift,
    SideStep,
    RingRaiseCombo,
    KneeLiftCombo,
    ChairPose,
    TreePose,
    HingePose,
    RevolvedCrescentLungePose,
    Warrior1Pose,
    Warrior2Pose,
    Warrior3Pose,
    FanPose,
    BoatPose,
    StandingForwardFold,
}
NAME_TO_FIT_SKILL = {
    skill.name: skill for skill in list(FIT_SKILLS)
}

def get_fit_skill_from_name(name: str) -> FitSkill:
    return NAME_TO_FIT_SKILL[name]

def is_fit_skill(name: str) -> bool:
    return name in NAME_TO_FIT_SKILL
