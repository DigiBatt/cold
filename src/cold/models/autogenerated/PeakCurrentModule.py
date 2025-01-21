
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricCurrentModule import ElectricCurrent



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class PeakCurrent(ElectricCurrent, ElectrochemicalQuantity):
    """
    Class representing the `PeakCurrent` entity, which inherits from:
    - ElectricCurrent, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_382b10dc_83aa_4e77_a1d5_1edd06fd1e05'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PeakCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PeakCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_382b10dc_83aa_4e77_a1d5_1edd06fd1e05',
    
    class_name='PeakCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_382b10dc_83aa_4e77_a1d5_1edd06fd1e05',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PeakCurrent',
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
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    