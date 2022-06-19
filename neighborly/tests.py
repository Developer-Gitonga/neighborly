from django.test import TestCase
from neighborly.models import Business, Contact, User, Profile,  NeighbourHood

# Create your tests here.


        
class Profile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='test bio', neighborhood=NeighbourHood.objects.create(name='test neighborhood', location='test location'))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_delete_profile(self):
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)
        
    def test_update_profile(self):
        self.profile.update_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
        
    def test_search_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.filter(bio__icontains='test').all()
        self.assertTrue(len(profile) > 0)
        
    def test_get_profile_by_id(self):
        self.profile.save_profile()
        profile = Profile.get_profile_by_id(self.user.id)
        self.assertTrue(len(profile) > 0)
        
    def test_get_profile_by_user(self):
        self.profile.save_profile()
        profile = Profile.get_profile_by_user(self.user)
        self.assertTrue(len(profile) > 0)
        
    def test_get_profile_by_neighborhood(self):
        self.profile.save_profile()
        profile = Profile.get_profile_by_neighborhood(self.profile.neighborhood)
        self.assertTrue(len(profile) > 0)
        

class Business(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='test bio', neighborhood=NeighbourHood.objects.create(name='test neighborhood', location='test location'))
        self.business = Business.objects.create(name='test business',email="test@gmail.com",neighborhood=self.profile.neighborhood,user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))
        
    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
        
    def test_delete_business(self):
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)
        
    def test_update_business(self):
        self.business.update_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)
        
    def test_search_business(self):
        self.business.save_business()
        business = Business.objects.filter(name__icontains='test').all()
        self.assertTrue(len(business) > 0)
        
    def test_get_business_by_id(self):
        self.business.save_business()
        business = Business.get_business_by_id(self.business.id)
        self.assertTrue(len(business) > 0)
        
    def test_get_business_by_user(self):
        self.business.save_business()
        business = Business.get_business_by_user(self.user)
        self.assertTrue(len(business) > 0)

    def test_get_business_by_neighborhood(self):
        self.business.save_business()
        business = Business.get_business_by_neighborhood(self.business.neighborhood)
        self.assertTrue(len(business) > 0)
        
    def test_get_business_by_email(self):
        self.business.save_business()
        business = Business.get_business_by_email(self.business.email)
        self.assertTrue(len(business) > 0)
        
    
class Contact(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='test bio', neighborhood=NeighbourHood.objects.create(name='test neighborhood', location='test location'))
        self.contact = Contact.objects.create(name='test contact',number="122222222",neighborhood=NeighbourHood.objects.create(name='test neighborhood', location='test location'))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.contact, Contact))
        
    def test_save_contact(self):
        self.contact.save_contact()
        contact = Contact.objects.all()
        self.assertTrue(len(contact) > 0)
        
    def test_delete_contact(self):
        self.contact.delete_contact()
        contact = Contact.objects.all()
        self.assertTrue(len(contact) == 0)
        
    def test_update_contact(self):
        self.contact.update_contact()
        contact = Contact.objects.all()
        self.assertTrue(len(contact) > 0)
        
    