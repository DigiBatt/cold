
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DiffusivityModule import Diffusivity







class ChargeCarrierDiffusivityInElectrolyte(Diffusivity):
    """
    Class representing the `ChargeCarrierDiffusivityInElectrolyte` entity, which inherits from:
    - Diffusivity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c274506_af5b_4ef1_8217_829ffd459f28'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargeCarrierDiffusivityInElectrolyte'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargeCarrierDiffusivityInElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c274506_af5b_4ef1_8217_829ffd459f28',
    
    class_name='ChargeCarrierDiffusivityInElectrolyte',
    
    cidemodKey="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    bpxKey="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4c274506_af5b_4ef1_8217_829ffd459f28',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargeCarrierDiffusivityInElectrolyte',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    

    
    

    

    