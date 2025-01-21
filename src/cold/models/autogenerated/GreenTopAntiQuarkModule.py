
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TopAntiQuarkModule import TopAntiQuark



from .GreenAntiQuarkModule import GreenAntiQuark







class GreenTopAntiQuark(TopAntiQuark, GreenAntiQuark):
    """
    Class representing the `GreenTopAntiQuark` entity, which inherits from:
    - TopAntiQuark, GreenAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_29836ff7_d416_49ae_b76b_f367c326b107'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenTopAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenTopAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_29836ff7_d416_49ae_b76b_f367c326b107',
    
    class_name='GreenTopAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_29836ff7_d416_49ae_b76b_f367c326b107',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenTopAntiQuark',
        alias="class_name"
    )
    

    
    

    

    