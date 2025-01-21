
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RealModule import Real



from .MetricPrefixModule import MetricPrefix







class SIPrefix(Real, MetricPrefix):
    """
    Class representing the `SIPrefix` entity, which inherits from:
    - Real, MetricPrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_23eabdb5_6de6_4615_b6b1_a07b3ad32fd9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIPrefix'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIPrefix(
    
    class_iri='https://w3id.org/emmo#EMMO_23eabdb5_6de6_4615_b6b1_a07b3ad32fd9',
    
    class_name='SIPrefix',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_23eabdb5_6de6_4615_b6b1_a07b3ad32fd9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIPrefix',
        alias="class_name"
    )
    

    
    

    

    