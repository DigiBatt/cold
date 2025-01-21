
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class MetalloidElementalSubstance(ElementalSubstance):
    """
    Class representing the `MetalloidElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a9a6507f_9c61_44d3_bd86_f1ebf763e150'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetalloidElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetalloidElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a9a6507f_9c61_44d3_bd86_f1ebf763e150',
    
    class_name='MetalloidElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a9a6507f_9c61_44d3_bd86_f1ebf763e150',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetalloidElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    