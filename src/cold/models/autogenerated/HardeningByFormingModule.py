
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialTreatmentModule import MaterialTreatment







class HardeningByForming(MaterialTreatment):
    """
    Class representing the `HardeningByForming` entity, which inherits from:
    - MaterialTreatment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_46dc0d51_b60f_49cd_8650_9aba7be3726c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HardeningByForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HardeningByForming(
    
    class_iri='https://w3id.org/emmo#EMMO_46dc0d51_b60f_49cd_8650_9aba7be3726c',
    
    class_name='HardeningByForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_46dc0d51_b60f_49cd_8650_9aba7be3726c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HardeningByForming',
        alias="class_name"
    )
    

    
    

    

    