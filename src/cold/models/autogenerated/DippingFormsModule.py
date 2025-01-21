
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromLiquidModule import FormingFromLiquid







class DippingForms(FormingFromLiquid):
    """
    Class representing the `DippingForms` entity, which inherits from:
    - FormingFromLiquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a09a5342_cad4_40fa_a619_a5af0867cb8f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DippingForms'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DippingForms(
    
    class_iri='https://w3id.org/emmo#EMMO_a09a5342_cad4_40fa_a619_a5af0867cb8f',
    
    class_name='DippingForms',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a09a5342_cad4_40fa_a619_a5af0867cb8f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DippingForms',
        alias="class_name"
    )
    

    
    

    

    