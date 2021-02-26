#!"C:\xampp\perl\bin\perl.exe"

use strict;
use DBI;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

print "Content-type: text/html\n\n";

### Read form Data
my $cgi = CGI->new;
my $designNo = $cgi->param('p');
my $as=$designNo;
my $dbh = DBI->connect("DBI:mysql:database=project;host=localhost",
                       "root", "",
                       {'RaiseError' => 1});

# now retrieve data from the table.
my $sth = $dbh->prepare("SELECT itemlist FROM franklin where Id = $designNo ");
$sth->execute();
while (my $ref = $sth->fetchrow_hashref()) {
  print "$ref->{'itemlist'}";
}
$sth->finish();

# Disconnect from the database.
$dbh->disconnect();