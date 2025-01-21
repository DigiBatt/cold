
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AmountConcentrationModule import AmountConcentration







class InitialChargeCarrierConcentrationInElectrolyte(AmountConcentration):
    """
    Class representing the `InitialChargeCarrierConcentrationInElectrolyte` entity, which inherits from:
    - AmountConcentration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_098f98dc_e015_4dbd_b358_a7ac3b3ecff3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InitialChargeCarrierConcentrationInElectrolyte'`
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
    obj = InitialChargeCarrierConcentrationInElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_098f98dc_e015_4dbd_b358_a7ac3b3ecff3',
    
    class_name='InitialChargeCarrierConcentrationInElectrolyte',
    
    cidemodKey="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    bpxKey="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_098f98dc_e015_4dbd_b358_a7ac3b3ecff3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InitialChargeCarrierConcentrationInElectrolyte',
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
    

    
    

    

    