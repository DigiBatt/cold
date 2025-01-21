
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class Magnetizing(MaterialTreatment):
    """
    Class representing the `Magnetizing` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c30aaeb1_66cc_4c69_8890_d7812c1d608c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Magnetizing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Magnetizing(
    
    class_iri='https://w3id.org/emmo#EMMO_c30aaeb1_66cc_4c69_8890_d7812c1d608c',
    
    class_name='Magnetizing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c30aaeb1_66cc_4c69_8890_d7812c1d608c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Magnetizing',
        alias="class_name"
    )
    

    
    

    

    