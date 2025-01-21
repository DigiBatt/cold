
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElementalSubstanceModule import ElementalSubstance







class NobleGasElementalSubstance(ElementalSubstance):
    """
    Class representing the `NobleGasElementalSubstance` entity, which inherits from:
    - ElementalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_cac14194_2d5f_4fe6_b794_a9319f6d76ee'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NobleGasElementalSubstance'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NobleGasElementalSubstance(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_cac14194_2d5f_4fe6_b794_a9319f6d76ee',
    
    class_name='NobleGasElementalSubstance',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_cac14194_2d5f_4fe6_b794_a9319f6d76ee',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NobleGasElementalSubstance',
        alias="class_name"
    )
    

    
    

    

    