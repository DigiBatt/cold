
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class PotentiometricSelectivityCoefficient(ElectrochemicalQuantity):
    """
    Class representing the `PotentiometricSelectivityCoefficient` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_136744ff_0563_4df7_aa03_4219d70392a0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotentiometricSelectivityCoefficient'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotentiometricSelectivityCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_136744ff_0563_4df7_aa03_4219d70392a0',
    
    class_name='PotentiometricSelectivityCoefficient',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_136744ff_0563_4df7_aa03_4219d70392a0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotentiometricSelectivityCoefficient',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    