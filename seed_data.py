import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GYM_MANAGEMENT_SYSTEM.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import (
    Banners, Service, Faq, Enquiry, MainLogo, Gallery, GalleryImages,
    SubscriptionPlans, SubscriptionPlansFeatures, Subscriber, SubscriptionType,
    Trainer, TrainerAcheivements, TrainerSalary, TrainerNotification, Notify,
    NotifUserStatus, AssignSubscriber
)
from datetime import date, datetime

def seed():
    print("Seeding database...")

    # Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Created superuser: admin / admin123")

    # Regular user
    user, created = User.objects.get_or_create(username='john_doe', defaults={
        'email': 'john@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    if created:
        user.set_password('password123')
        user.save()
        print("Created user: john_doe / password123")

    # Main Logo
    if not MainLogo.objects.exists():
        MainLogo.objects.create(logo_image='main_logo/45671.jpg')
        print("Created MainLogo")

    # Banners
    Banners.objects.all().delete()
    Banners.objects.create(img='banners/banner_img1.jpg', alt_text='Unleash Your Inner Strength')
    Banners.objects.create(img='banners/banner_img2.jpg', alt_text='Transform Your Body & Mind')
    Banners.objects.create(img='banners/banner_img3.jpg', alt_text='Elite Performance Equipment')
    print("Created Banners")

    # Services
    if not Service.objects.exists():
        Service.objects.create(
            title='Strength & Hypertrophy',
            details='Customized progressive overload routines designed to build pure muscle density and increase core power.',
            img='services/service1.jpg'
        )
        Service.objects.create(
            title='Cardio & HIIT Conditioning',
            details='High-energy endurance and interval sessions that torch body fat, elevate stamina, and boost heart health.',
            img='services/service2.jpg'
        )
        Service.objects.create(
            title='Personalized Nutrition & Coaching',
            details='One-on-one tailored macro guidance, bi-weekly physical assessments, and dedicated mentor accountability.',
            img='services/service3.jpg'
        )
        print("Created Services")

    # FAQs
    if not Faq.objects.exists():
        Faq.objects.create(
            question='What are the gym operating hours?',
            answer='We are open 24/7 for all members with card or mobile pass access, with staffed hours from 6 AM to 10 PM daily.'
        )
        Faq.objects.create(
            question='Do you offer free trial passes?',
            answer='Yes! New visitors can request a complimentary 3-day guest pass by submitting the enquiry form or visiting our front desk.'
        )
        Faq.objects.create(
            question='Can I switch or freeze my membership plan?',
            answer='You can easily freeze or upgrade your subscription from your dashboard or by speaking to member support.'
        )
        Faq.objects.create(
            question='Are personal trainers included in standard packages?',
            answer='Premium and VIP Elite plans come with dedicated personal trainer matching and customized workout schedules.'
        )
        print("Created FAQs")

    # Pricing Plans & Features
    if not SubscriptionPlans.objects.exists():
        basic = SubscriptionPlans.objects.create(
            title='Starter Fitness',
            price=29,
            max_members=50,
            highlight_status=False,
            validity=30
        )
        pro = SubscriptionPlans.objects.create(
            title='Pro Athlete',
            price=59,
            max_members=100,
            highlight_status=True,
            validity=30
        )
        vip = SubscriptionPlans.objects.create(
            title='VIP Elite Coaching',
            price=99,
            max_members=30,
            highlight_status=False,
            validity=30
        )

        f1 = SubscriptionPlansFeatures.objects.create(title='Full Access to All Gym Facilities')
        f2 = SubscriptionPlansFeatures.objects.create(title='Locker & Sauna Access')
        f3 = SubscriptionPlansFeatures.objects.create(title='Free Functional Training Classes')
        f4 = SubscriptionPlansFeatures.objects.create(title='1-on-1 Dedicated Trainer Assignment')
        f5 = SubscriptionPlansFeatures.objects.create(title='Weekly Nutrition & Macro Audit')
        f6 = SubscriptionPlansFeatures.objects.create(title='Unlimited Guest Passes & Body Scan')

        f1.subplan.add(basic, pro, vip)
        f2.subplan.add(basic, pro, vip)
        f3.subplan.add(pro, vip)
        f4.subplan.add(pro, vip)
        f5.subplan.add(vip)
        f6.subplan.add(vip)
        print("Created Plans & Features")
    else:
        pro = SubscriptionPlans.objects.filter(highlight_status=True).first() or SubscriptionPlans.objects.first()

    # Trainer
    trainer, t_created = Trainer.objects.get_or_create(username='alex_fit', defaults={
        'full_name': 'Alex Sterling',
        'password': 'trainer123',
        'mobile': 9876543210,
        'address': '45 Fitness Boulevard, Suite 10, Metro City',
        'is_active': True,
        'details': 'Certified CSCS strength coach with 8+ years specializing in hypertrophy, body recomposition, and athlete conditioning.',
        'img': 'trainers/portrait-handsome-man.jpg',
        'social_links': {
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'linkedin': 'https://linkedin.com'
        },
        'month_salary': 3500
    })
    if t_created:
        print("Created Trainer: alex_fit / trainer123")

    # Trainer Achievements
    if not TrainerAcheivements.objects.filter(trainer=trainer).exists():
        TrainerAcheivements.objects.create(
            trainer=trainer,
            title='National Strength Coach of the Year',
            date_awarded=date(2023, 6, 15),
            description='Awarded for exceptional client transformation milestones and advanced biomechanics education.',
            badge_image='achievement_badges/Picture1.jpg'
        )
        TrainerAcheivements.objects.create(
            trainer=trainer,
            title='Master Kettlebell & Functional Specialist',
            date_awarded=date(2022, 11, 20),
            description='Certified elite mobility instructor with Olympic lifting credential.',
            badge_image='achievement_badges/minimal-abstract-logo-gym_658271-5156.jpg'
        )
        print("Created Trainer Achievements")

    # Trainer Salary
    if not TrainerSalary.objects.filter(trainer=trainer).exists():
        TrainerSalary.objects.create(
            trainer=trainer,
            amount=3500,
            deposit_date=datetime(2024, 1, 1, 10, 0),
            remarks='Monthly basic retainer + client milestone bonus'
        )
        TrainerSalary.objects.create(
            trainer=trainer,
            amount=3500,
            deposit_date=datetime(2024, 2, 1, 10, 0),
            remarks='Monthly regular salary deposit'
        )
        print("Created Trainer Salary entries")

    # User Subscription
    if not SubscriptionType.objects.filter(user=user).exists():
        sub_type = SubscriptionType.objects.create(
            user=user,
            plan=pro,
            price=pro.price,
            reg_date=date.today()
        )
        print("Created Subscription for user")
    else:
        sub_type = SubscriptionType.objects.filter(user=user).first()

    # Assign Subscriber to Trainer
    if not AssignSubscriber.objects.filter(trainer=trainer, subscriber=sub_type).exists():
        AssignSubscriber.objects.create(
            subscriber=sub_type,
            trainer=trainer
        )
        print("Assigned subscriber to trainer")

    # Subscriber profile
    if not Subscriber.objects.filter(user=user).exists():
        Subscriber.objects.create(
            user=user,
            mobile='555-0199',
            address='12 Greenway Blvd, Downtown',
            img='subs/profile-pic.png'
        )
        print("Created Subscriber profile")

    # Gallery & GalleryImages
    if not Gallery.objects.exists():
        g1 = Gallery.objects.create(
            title='State-of-the-Art Gym Floor',
            details='Tour our Olympic-grade free weights, Hammer Strength racks, and premium cardio stations.',
            img='gallery/fitness-equipment.jpg'
        )
        g2 = Gallery.objects.create(
            title='High Energy Group Classes',
            details='Experience pulse-pounding spinning, functional HIIT, and yoga mobility sessions with elite instructors.',
            img='gallery/full-shot-fit-people-gym.jpg'
        )
        g3 = Gallery.objects.create(
            title='Member Transformations',
            details='Real members, real results: explore inspirational health and strength milestones achieved at RJ Gym.',
            img='gallery/trans4.jpg'
        )

        GalleryImages.objects.create(gallery=g1, alt_text='Dumbbell Area', img='gallery_imgs/dumbbells-arrangement-gym.jpg')
        GalleryImages.objects.create(gallery=g1, alt_text='3D Equipment', img='gallery_imgs/3d-gym-equipment.jpg')
        GalleryImages.objects.create(gallery=g1, alt_text='Gym Interior', img='gallery_imgs/gym-interior-with-equipment.jpg')
        GalleryImages.objects.create(gallery=g2, alt_text='Group Workout', img='gallery_imgs/people-working-out-indoors-together-with-dumbbells.jpg')
        GalleryImages.objects.create(gallery=g2, alt_text='Team Training', img='gallery_imgs/side-view-people-training-together-gym.jpg')
        GalleryImages.objects.create(gallery=g3, alt_text='Transformation 1', img='gallery_imgs/trans1.jpeg')
        GalleryImages.objects.create(gallery=g3, alt_text='Transformation 2', img='gallery_imgs/trans2.jpg')
        print("Created Galleries & Images")

    # Notifications
    if not TrainerNotification.objects.exists():
        TrainerNotification.objects.create(notif_msg='New member John Doe assigned to your training roster.')
        TrainerNotification.objects.create(notif_msg='Monthly coaching feedback reports are due this Friday.')
        print("Created Trainer Notifications")

    if not Notify.objects.exists():
        n1 = Notify.objects.create(notify_detail='Welcome to RJ GYM! Schedule your initial fitness consultation.')
        n2 = Notify.objects.create(notify_detail='New functional training workshop starts this Saturday at 10 AM.')
        NotifUserStatus.objects.create(notif=n1, user=user, status=False)
        NotifUserStatus.objects.create(notif=n2, user=user, status=False)
        print("Created User Notifications")

    print("Seeding complete successfully!")

if __name__ == '__main__':
    seed()
