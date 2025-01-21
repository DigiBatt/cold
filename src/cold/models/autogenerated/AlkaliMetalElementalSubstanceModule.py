
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class AlkaliMetalElementalSubstance(ElementalSubstance):
    """
    Class representing the `AlkaliMetalElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_68e4028b_0ec6_46da_8d1c_d00c644e8c82'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkaliMetalElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkaliMetalElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_68e4028b_0ec6_46da_8d1c_d00c644e8c82',
    
    class_name='AlkaliMetalElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_68e4028b_0ec6_46da_8d1c_d00c644e8c82',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkaliMetalElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    